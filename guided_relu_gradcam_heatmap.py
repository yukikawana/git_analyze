#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import tensorflow as tf
from segnet import segnet
from tensorflow.contrib.keras import backend as K
from PIL import Image
import numpy as np
import pdb
import cv2
from vis.visualization import visualize_activation_tf
from vis.input_modifiers import Jitter
from PIL import Image
from vis.utils import utils
from vis.visualization import visualize_activation
from vis.input_modifiers import Jitter
import sys, os
import tensorflow.contrib.slim as slim
from tensorflow.python.framework import ops
from tensorflow.python.ops import gen_nn_ops

@ops.RegisterGradient("GuidedRelu")
def _GuidedReluGrad(op, grad):
    return tf.where(0. < grad, gen_nn_ops._relu_grad(grad, op.outputs[0]), tf.zeros(grad.get_shape()))

def get_img(idx, name):
    #img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, tv_weight=.0,lp_norm_weight=10., input_modifiers=[Jitter(0.05)],max_iter=500, verbose=True)
    #img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx,seed_input=img, max_iter=600, act_max_weight=1.,tv_weight=0.01,lp_norm_weight=10, input_modifiers=[Jitter(16)], verbose=True)
    img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, max_iter=600, act_max_weight=1.,tv_weight=0.01,lp_norm_weight=10, input_modifiers=[Jitter(16)], verbose=True)
#    img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, max_iter=1800, act_max_weight=1.,tv_weight=0.01,lp_norm_weight=10000, input_modifiers=[Jitter(16)], verbose=True)
    return img

 #define input shape
input_shape = (360, 480)

#construct graph
inputs = tf.placeholder("float", shape=(1, input_shape[0], input_shape[1], 3))
logits, end_points = segnet(inputs)
outputs = tf.argmax(logits)
sess = tf.Session()
saver = tf.train.Saver()
saver.restore(sess,'weights/segnet_tf.ckpt')
K.set_session(sess)
K.manual_variable_initialization(True)
#visualize filters
name = 'conv4_2_bn'
name = 'relu_2'
name = 'conv4_2'

name = 'conv5_3'
name = 'relu5_3'
name = 'relu3_3'
name = 'relu5_3'
name = 'conv1_1_D'
cvimg = cv2.resize(cv2.imread('car2.png'), (input_shape[1], input_shape[0]))
nimage = cvimg
nimage = np.expand_dims(nimage,0 )
obj = 9
idx_index = 0

outputs = tf.argmax(logits, axis=3)
fn=K.function([inputs],[outputs])
mask = np.squeeze(np.asarray(fn([nimage])))
Image.fromarray(np.uint8(mask/11.*255)).save('recog.png')
mask[mask != obj] = 0
mask[mask == obj] = 1
Image.fromarray(np.uint8(mask/11.*255)).save('mask.png')
masks = np.zeros([1,input_shape[0], input_shape[1], 12])
masks[:,:,:,obj] = mask
signal = tf.multiply(logits, masks)
loss = tf.reduce_mean(signal)
grads = tf.gradients(loss, end_points[name])[0]
# Normalizing the gradients
norm_grads = tf.div(grads, tf.sqrt(tf.reduce_mean(tf.square(grads))) + tf.constant(1e-5))
#grads_val, layer = sess.run([norm_grads, end_points[name]], feed_dict={inputs: nimage})
fn=K.function([inputs],[end_points[name]])
layer = fn([nimage])
layer = np.squeeze(layer)
grads_val = sess.run([norm_grads], feed_dict={inputs: nimage})
grads_val = grads_val[0]
weights = np.mean(grads_val, axis = (0, 1, 2)) 			# [512]
idxs = np.argsort(weights)[::-1]
idx = idxs[idx_index]

#apply guided relu to intermiediate layer
#eval_graph = tf.get_default_graph()
#with eval_graph.as_default():
img = get_img(idx, name)
with tf.get_default_graph().gradient_override_map({'Relu': 'GuidedRelu'}):
    #    guided_relu_logits, guided_relu_end_points = segnet(inputs)
    #    guided_relu_outputs = tf.argmax(guided_relu_logits)
    guided_relu_signal = end_points[name][:,:,:,idx]
    guided_relu_loss = tf.reduce_mean(guided_relu_signal)
    gr_grads = tf.gradients(guided_relu_loss, inputs)[0]

saver = tf.train.Saver()
gr_grads_val = sess.run([gr_grads], feed_dict={inputs: nimage})
gr_grads_val = np.asarray(gr_grads_val)
gr_grads_val = np.squeeze(gr_grads_val)
print 'grval', gr_grads_val.shape
print 'nimage', nimage.shape
gr_grads_val= np.dstack((
        gr_grads_val[:, :, 2],
        gr_grads_val[:, :, 1],
        gr_grads_val[:, :, 0],
    ))
gr_grads_val= (gr_grads_val- np.min(gr_grads_val, axis=(0, 1)))/np.ptp(gr_grads_val)*255
layer = np.asarray(layer)
channel = np.squeeze(layer[:,:,idx])
channel = (channel - np.min(channel, axis=(0, 1)))/np.ptp(channel)
channel255 = channel*255
channel_resized = cv2.resize(channel,(input_shape[1], input_shape[0]))
#gr_grads_val[:, :, 0]= np.multiply(gr_grads_val[:, :, 0],channel_resized)
#gr_grads_val[:, :, 1]=np.multiply(gr_grads_val[:, :, 1],channel_resized)
#gr_grads_val[:, :, 2]=np.multiply(gr_grads_val[:, :, 2],channel_resized)
cam_heatmap = cv2.resize(cv2.applyColorMap(np.uint8(channel255), cv2.COLORMAP_JET), (input_shape[1], input_shape[0]))
print cam_heatmap.shape
print cvimg.shape
cc = cam_heatmap*0.5+cvimg+0.5
cc = np.float32(cc)/np.max(cc,axis=(0,1,2))*255
cv2.imwrite('{}_{}_heatmap.png'.format(name,idx),np.uint8(cc))
cv2.imwrite('{}_{}_grmap.png'.format(name,idx),np.uint8(gr_grads_val))
Image.fromarray(np.uint8(img)).save('{}_{}.png'.format(name,idx))
print idx, name

 
