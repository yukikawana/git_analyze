#from tensorflow.contrib.keras.applications import VGG16
import numpy as np
from PIL import Image
from vis.utils import utils
from tensorflow.contrib.keras import activations
from tensorflow.contrib.keras.python.keras.models import load_model
from vis.visualization import visualize_activation
from vis.input_modifiers import Jitter
import sys, os

vgg_path='vgg16.h5'
if os.path.exists(vgg_path):
    model=load_model(vgg_path) 
else:
    print 'vgg16 model not found, downloading...'
    model = VGG16(weights='imagenet', include_top=True)
    model.save(vgg_path)
    
layer_idx = utils.find_layer_idx(model, 'predictions')
model.layers[layer_idx].activation = activations.linear
model = utils.apply_modifications(model)
layer_idx = utils.find_layer_idx(model, 'block5_conv3')
#layer_idx = utils.find_layer_idx(model, 'block5_conv3')
idx=454
seed = visualize_activation(model, layer_idx, filter_indices=idx,tv_weight=0., input_modifiers=[Jitter(0.05)])
img = visualize_activation(model, layer_idx, max_iter=100,filter_indices=idx,seed_input=seed,  input_modifiers=[Jitter(16)], verbose=True)
#img = visualize_activation(model, layer_idx,max_iter=500, filter_indices=idx, input_modifiers=[Jitter(0.05)])
#img = visualize_activation(model, layer_idx,max_iter=10000, filter_indices=idx, input_modifiers=[Jitter(16)])
Image.fromarray(np.uint8(img)).save('am.png')
#img = visualize_activation(model, layer_idx, filter_indices=20, max_iter=500, input_modifiers=[Jitter(16)])

