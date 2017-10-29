#!/usr/bin/python
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
 #define input shape
input_shape = (360, 480)

#construct graph
inputs = tf.placeholder("float", shape=(1, input_shape[0], input_shape[1], 3))
logits, end_points = segnet(inputs)
print logits
outputs = tf.argmax(logits)
sess = tf.Session()
saver = tf.train.Saver()
saver.restore(sess,'weights/segnet_tf.ckpt')
K.set_session(sess)
K.manual_variable_initialization(True)
#visualize filters
name = 'conv1_1_D'
name = 'conv4_2_bn'
name = 'relu_2'
name = 'conv4_2'
name = 'relu5_3'
name = 'conv2_1_D'
name = 'conv5_3'
name = 'relu5_3'
idx =8
#img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, tv_weight=.0,lp_norm_weight=0., input_modifiers=[Jitter(0.05)])
#img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, max_iter=1800, act_max_weight=0.1,tv_weight=0.01,lp_norm_weight=10000, input_modifiers=[Jitter(16)], verbose=True)
#Image.fromarray(np.uint8(img)).save('{}_{}.png'.format(name,idx))

#nimage = np.asarray([Image.open('test.png').resize(input_shape).getdata()]).astype(np.float32)
#nimage = np.reshape(nimage,(input_shape[0],input_shape[1],3))
nimage = cv2.resize(cv2.imread('car.png'), (input_shape[1], input_shape[0]))
nimage = np.expand_dims(nimage,0 )

outputs = tf.argmax(logits, axis=3)
fn=K.function([inputs],[outputs])
mask = np.squeeze(np.asarray(fn([nimage])))
mask[mask != 9] = 1
mask[mask == 1] = 1
masks = np.zeros([1,input_shape[0], input_shape[1], 12])
print masks.shape
masks[:,:,:,9] = mask
signal = tf.multiply(logits, masks)
loss = tf.reduce_mean(signal)
grads = tf.gradients(loss, end_points[name])[0]
# Normalizing the gradients
norm_grads = tf.div(grads, tf.sqrt(tf.reduce_mean(tf.square(grads))) + tf.constant(1e-5))
grads_val = sess.run([norm_grads], feed_dict={inputs: nimage})
grads_val = grads_val[0]
print grads_val.shape
weights = np.mean(grads_val, axis = (0, 1, 2)) 			# [512]
print weights.shape
idxs = np.argsort(weights)[::-1]
idx = idxs[0]
print idx, name
def get_img(idx, name):
    img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, tv_weight=.0,lp_norm_weight=10., input_modifiers=[Jitter(0.05)],max_iter=200, verbose=True)
    img = visualize_activation_tf(inputs,end_points,name, seed_input=img,filter_indices=idx, max_iter=600, act_max_weight=1.,tv_weight=0.01,lp_norm_weight=10, input_modifiers=[Jitter(16)], verbose=True)
#    img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, max_iter=600, act_max_weight=1.,tv_weight=0.01,lp_norm_weight=10, input_modifiers=[Jitter(16)], verbose=True)
    return img
img = get_img(idx, name)
Image.fromarray(np.uint8(img)).save('{}_{}.png'.format(name,idx))

idx = idxs[1]
print idx, name
img = get_img(idx, name)
Image.fromarray(np.uint8(img)).save('{}_{}.png'.format(name,idx))
 
