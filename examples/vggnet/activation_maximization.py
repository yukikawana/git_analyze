
# coding: utf-8

# # Activation Maximization on VGGNet

# ## Dense Layer Visualizations

# To visualize activation over final dense layer outputs, we need to switch the `softmax` activation out for `linear` since gradient of output node will depend on all the other node activations. Doing this in keras is tricky, so we provide `utils.apply_modifications` to modify network parameters and rebuild the graph.
# 
# If this swapping is not done, the results might be suboptimal. We will start by swapping out 'softmax' for 'linear' and compare what happens if we dont do this at the end.

# In[8]:


from keras.applications import VGG16
from vis.utils import utils
from keras import activations

# Build the VGG16 network with ImageNet weights
model = VGG16(weights='imagenet', include_top=True)

# Utility to search for layer index by name. 
# Alternatively we can specify this as -1 since it corresponds to the last layer.
layer_idx = utils.find_layer_idx(model, 'predictions')

# Swap softmax with linear
model.layers[layer_idx].activation = activations.linear
model = utils.apply_modifications(model)


# ### Visualizing a specific output category

# Lets try visualizing a specific output category. We will pick `ouzel` which corresponds to imagenet category `20`

# In[9]:


from vis.visualization import visualize_activation

from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')
plt.rcParams['figure.figsize'] = (18, 6)

# 20 is the imagenet category for 'ouzel'
img = visualize_activation(model, layer_idx, filter_indices=20)
plt.imshow(img)


# Hmm, that sort of looks like a bird. Lets see if we can get better results with more iterations. This time, lets see the verbose output during the optimization process.

# In[10]:


# 20 is the imagenet category for 'ouzel'
img = visualize_activation(model, layer_idx, filter_indices=20, max_iter=500, verbose=True)
plt.imshow(img)


# We can see that the loss appears to be converging. So more iterations definitely seem to give better output. One way to get crisper results is to use `Jitter` input_modifier. As the name suggests, `Jitter` moves pixels around in the image. Lets try this out.

# In[11]:


from vis.input_modifiers import Jitter

# 20 is the imagenet category for 'ouzel'
# Jitter 16 pixels along all dimensions to during the optimization process.
img = visualize_activation(model, layer_idx, filter_indices=20, max_iter=500, input_modifiers=[Jitter(16)])
plt.imshow(img)


# Look at that! Not only has the conv net captured what it means to be an ouzel, but it also seems to encode for different orientations and scales, a further proof of rotational and scale invariance. 

# Lets try this for a bunch of other random categories. This will take a while. Go grab a nice cup of coffee and prepare to be amused :)

# In[12]:


import numpy as np
categories = np.random.permutation(1000)[:15]

vis_images = []
image_modifiers = [Jitter(16)]
for idx in categories:    
    img = visualize_activation(model, layer_idx, filter_indices=idx, max_iter=500, input_modifiers=image_modifiers)
    
    # Reverse lookup index to imagenet label and overlay it on the image.
    img = utils.draw_text(img, utils.get_imagenet_label(idx))
    vis_images.append(img)

# Generate stitched images with 5 cols (so it will have 3 rows).
plt.rcParams['figure.figsize'] = (50, 50)
stitched = utils.stitch_images(vis_images, cols=5)
plt.axis('off')
plt.imshow(stitched)
plt.show()


# Some of them make sense if you stare at ot for a while. There are ways of improving this. We will cover some ideas for this in the next section. You can come back here and try those out as an exercise.

# ## Visualizing Conv filters

# In a CNN, each Conv layer has several learned *template matching* filters that maximize their output when a similar 
# template pattern is found in the input image. First Conv layer is easy to interpret; simply visualize the weights as an image. To see what the Conv layer is doing, a simple option is to apply the filter over raw input pixels. 
# Subsequent Conv filters operate over the outputs of previous Conv filters (which indicate the presence or absence 
# of some templates), making them hard to interpret.
# 
# One way of interpreting them is to generate an input image that maximizes the filter output. This allows us to generate an input that activates the filter.
# 
# Lets start by visualizing the second conv layer of vggnet (named as 'block1_conv2'). Here is the VGG16 model for reference.

# In[13]:


model.summary()


# In[14]:


from vis.visualization import get_num_filters

# The name of the layer we want to visualize
# You can see this in the model definition.
layer_name = 'block1_conv2'
layer_idx = utils.find_layer_idx(model, layer_name)

# Visualize all filters in this layer.
filters = np.arange(get_num_filters(model.layers[layer_idx]))

# Generate input image for each filter.
vis_images = []
for idx in filters:
    img = visualize_activation(model, layer_idx, filter_indices=idx)
    
    # Utility to overlay text on image.
    img = utils.draw_text(img, 'Filter {}'.format(idx))    
    vis_images.append(img)

# Generate stitched image palette with 8 cols.
stitched = utils.stitch_images(vis_images, cols=8)    
plt.axis('off')
plt.imshow(stitched)
plt.title(layer_name)
plt.show()


# They mostly seem to match for specific color and directional patterns. Lets try a bunch of other layers.
# We will randomly visualize 10 filters within various layers.

# In[15]:


selected_indices = []
for layer_name in ['block2_conv2', 'block3_conv3', 'block4_conv3', 'block5_conv3']:
    layer_idx = utils.find_layer_idx(model, layer_name)

    # Visualize all filters in this layer.
    filters = np.random.permutation(get_num_filters(model.layers[layer_idx]))[:10]
    selected_indices.append(filters)

    # Generate input image for each filter.
    vis_images = []
    for idx in filters:
        img = visualize_activation(model, layer_idx, filter_indices=idx)

        # Utility to overlay text on image.
        img = utils.draw_text(img, 'Filter {}'.format(idx))    
        vis_images.append(img)

    # Generate stitched image palette with 5 cols so we get 2 rows.
    stitched = utils.stitch_images(vis_images, cols=5)    
    plt.figure()
    plt.axis('off')
    plt.imshow(stitched)
    plt.show()


# We can see how filters evolved to look for simple -> complex abstract patterns.
# 
# We also notice that some of the filters in `block5_conv3` (the last one) failed to converge.  This is usually because regularization losses (total variation and LP norm) are overtaking activation maximization loss (set verbose=True to observe). There are a couple of options to make this work better,
# 
# - Different regularization weights.
# - Increase number of iterations.
# - Add `Jitter` input_modifier.
# - Try with 0 regularization weights, generate a converged image and use that as `seed_input` with regularization enabled.

# I will show a subset of these ideas here. Lets start by adidng Jitter and disabling total variation.

# In[16]:


layer_idx = utils.find_layer_idx(model, 'block5_conv3')

# We need to select the same random filters in order to compare the results.
filters = selected_indices[-1]
selected_indices.append(filters)

# Generate input image for each filter.
vis_images = []
for idx in filters:
    # We will jitter 5% relative to the image size.
    img = visualize_activation(model, layer_idx, filter_indices=idx, 
                               tv_weight=0.,
                               input_modifiers=[Jitter(0.05)])

    # Utility to overlay text on image.
    img = utils.draw_text(img, 'Filter {}'.format(idx))    
    vis_images.append(img)

# Generate stitched image palette with 5 cols so we get 2 rows.
stitched = utils.stitch_images(vis_images, cols=5)    
plt.figure()
plt.axis('off')
plt.imshow(stitched)
plt.show()


# We can see how previously unconverged filters show something this time. Lets take a specific output from here and use it as a `seed_input` with total_variation enabled this time.

# In[17]:


# Generate input image for each filter.
new_vis_images = []
for i, idx in enumerate(filters):
    # We will seed with optimized image this time.
    img = visualize_activation(model, layer_idx, filter_indices=idx, 
                               seed_input=vis_images[i],
                               input_modifiers=[Jitter(0.05)])

    # Utility to overlay text on image.
    img = utils.draw_text(img, 'Filter {}'.format(idx))    
    new_vis_images.append(img)

# Generate stitched image palette with 5 cols so we get 2 rows.
stitched = utils.stitch_images(new_vis_images, cols=5)    
plt.figure()
plt.axis('off')
plt.imshow(stitched)
plt.show()


# And that, folks, is how we roll :)
# This trick works pretty well to get those stubborn filters to converge.

# ## Other fun stuff

# The API to `visualize_activation` accepts `filter_indices`. This is generally meant for *multi label* classifiers, but nothing prevents us from having some fun. 
# 
# By setting `filter_indices`, to multiple output categories, we can generate an input that the network thinks is both those categories. Maybe we can generate a cool looking crab fish. I will leave this as an exersice to the reader. You mgith have to experiment with regularization weights a lot.
# 
# Ideally, we can use a GAN trained on imagenet and use the discriminator loss as a regularizer. This is easily done using `visualize_activations_with_losses` API. If you ever do this, please consider submitting a PR :)

# ## Visualizations without swapping softmax

# As alluded at the beginning of the tutorial, we want to compare and see what happens if we didnt swap out softmax for linear activation.
# 
# Lets try the `ouzel` visualization again.

# In[21]:


layer_idx = utils.find_layer_idx(model, 'predictions')

# Swap linear back with softmax
model.layers[layer_idx].activation = activations.softmax
model = utils.apply_modifications(model)

img = visualize_activation(model, layer_idx, filter_indices=20, input_modifiers=[Jitter(16)])
plt.rcParams['figure.figsize'] = (18, 6)
plt.imshow(img)


# It does not work! The reason is that maximizing an output node can be done by minimizing other outputs. Softmax is weird that way. It is the only activation that depends on other node output(s) in the layer.
