
# coding: utf-8

# # GradCAM Visualization Demo with VGG16
# 

# In[1]:


# Replace vanila relu to guided relu to get guided backpropagation.
import tensorflow as tf

from tensorflow.python.framework import ops
from tensorflow.python.ops import gen_nn_ops
from tensorflow.contrib.keras import backend as K

@ops.RegisterGradient("GuidedRelu")
def _GuidedReluGrad(op, grad):
    return tf.where(0. < grad, gen_nn_ops._relu_grad(grad, op.outputs[0]), tf.zeros(grad.get_shape()))


# In[26]:



import numpy as np
from segnet import segnet
import utils
import cv2
import matplotlib.pyplot as plt
from vis.visualization import visualize_activation_tf
from vis.input_modifiers import Jitter
from PIL import Image
import sys, os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Create mini-batch for demo

def get_img(idx, name):
    img = visualize_activation_tf(inputs,visend_points,name, filter_indices=idx, max_iter=200, act_max_weight=20.,tv_weight=0.01,lp_norm_weight=10, input_modifiers=[Jitter(16)], verbose=True)
    #seed = visualize_activation_tf(inputs, end_points, name, filter_indices=idx,tv_weight=0.,act_max_weight=100., input_modifiers=[Jitter(0.05)],verbose=True)

input_shape = (360, 480)

batch_img = cv2.resize(cv2.imread('car2.png'), (input_shape[1], input_shape[0]))

batch_img = np.expand_dims(batch_img,0 )
batch_size = 1
idxs =[386,478,233,430,111,227,7,417,298,368]
idxs =[89,137,71,211,160,181,63,231,155,117]
top = 10
idx = 1
name = 'conv4_2'
name = 'conv3_3_D'
name = 'conv5_3'
obj = 9

# Create tensorflow graph for evaluation
eval_graph = tf.Graph()
with eval_graph.as_default():
    with eval_graph.gradient_override_map({'Relu': 'GuidedRelu'}):
    
        images = tf.placeholder("float", [batch_size, input_shape[0], input_shape[1], 3])
        masks = tf.placeholder("float", [batch_size, input_shape[0], input_shape[1],12])

        logits, end_points = segnet(images)
        prob = tf.nn.softmax(logits)
        argmax = tf.argmax(logits, axis=3)
        #visualize filters
        #masks = np.zeros([1,input_shape[0], input_shape[1], 12])
        #masks[:,:,:,9] = np.ones([1, input_shape[0], input_shape[1]])

        cost = tf.reduce_sum(tf.multiply(prob, masks))
        grad_for_weighting = tf.nn.relu(tf.gradients(cost, end_points[name])[0])
        pixelwise_weight = tf.multiply(grad_for_weighting, end_points[name])
        weights = tf.squeeze(tf.reduce_mean(pixelwise_weight, axis=(1,2)))
        sorted_weights, indices = tf.nn.top_k(weights, weights.get_shape()[0])

        layer_shape = end_points[name].get_shape().as_list()
        resized_mask = tf.image.resize_nearest_neighbor(masks,layer_shape[1:3])
        print resized_mask
        cost2 = tf.reduce_max(tf.multiply(end_points[name][:,:,:,indices[idx]],resized_mask[:,:,:,obj]), axis=(1,2))
        #cost2 = tf.reduce_max(end_points[name][:,:,:,indices[idx]], axis=(1,2))

        # Get last convolutional layer gradient for generating gradCAM visualization
        target_conv_layer = end_points['conv1_1_D']
        #target_conv_layer = vgg.conv3_2
        target_conv_layer_grad = tf.gradients(cost, target_conv_layer)[0]

        # Guided backpropagtion back to input layer
        gb_grad = tf.gradients(cost2, images)[0]

        # Normalizing the gradients    
        target_conv_layer_grad_norm = tf.div(target_conv_layer_grad, tf.sqrt(tf.reduce_mean(tf.square(target_conv_layer_grad))) + tf.constant(1e-5))


        init = tf.global_variables_initializer()

        
# Run tensorflow 

with tf.Session(graph=eval_graph) as sess:    
    saver = tf.train.Saver()
    saver.restore(sess,'weights/segnet_tf.ckpt')
    #sess.run(init)
    
    
    #compute mask for final output
    argmax_value = sess.run([argmax], feed_dict={images: batch_img})[0]
    npmasks = np.zeros([1,input_shape[0], input_shape[1], 12])
    npmask = np.zeros([1,input_shape[0], input_shape[1]])
    npmask[argmax_value==obj] = 1
    npmasks[:,:,:,obj] = npmask
    #gb_grad_value, target_conv_layer_value, target_conv_layer_grad_value, indices_value, weights_value = sess.run([gb_grad, target_conv_layer, target_conv_layer_grad_norm, indices, sorted_weights], feed_dict={images: batch_img})
    gb_grad_value, target_conv_layer_value, target_conv_layer_grad_value, indices_value, weights_value = sess.run([gb_grad, target_conv_layer, target_conv_layer_grad_norm, indices, sorted_weights], feed_dict={images: batch_img, masks: npmasks})
    print indices_value
    weights_sorted = np.sort(weights_value)[::-1]
    percentage_pre = (weights_sorted - np.min(weights_sorted))/np.ptp(weights_sorted)
    percentage = percentage_pre/np.sum(percentage_pre)
#    plt.plot(percentage)
    #plt.plot(np.cumsum(percentage))
#    plt.savefig("savefig.png")

    for i in range(batch_size):
        print 'visualize'
        utils.visualize(batch_img[i], target_conv_layer_value[i], target_conv_layer_grad_value[i], gb_grad_value[i])
print 'visualize done'

#visualizing part    
"""
inputs = tf.placeholder("float", [batch_size, input_shape[0], input_shape[1], 3])
vislogits, visend_points = segnet(inputs)
sess = tf.Session()
saver = tf.train.Saver()
saver.restore(sess,'weights/segnet_tf.ckpt')
K.set_session(sess)
K.manual_variable_initialization(True)
img = get_img(indices_value[idx], name)
print img
print indices_value[idx], name
Image.fromarray(np.uint8(img)).save('vised/{}_{}.png'.format(name,indices_value[idx]))
"""

