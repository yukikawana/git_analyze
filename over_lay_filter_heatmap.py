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


 #define input shape
input_shape = (360, 480)

#construct graph
inputs = tf.placeholder("float", shape=(1, input_shape[0], input_shape[1], 3))
logits, end_points = segnet(inputs)
print logits
prob = tf.nn.softmax(logits)
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
name = 'relu1_2_D'
name = 'relu4_3'
name = 'relu5_3'
name = 'conv5_3'
name = 'conv5_1'
name = 'conv3_3_D'
cvimg = cv2.resize(cv2.imread('car2.png'), (input_shape[1], input_shape[0]))
nimage = cvimg
nimage = np.expand_dims(nimage,0 )
obj = 9

outputs = tf.argmax(logits, axis=3)
fn=K.function([inputs],[outputs])
mask = np.squeeze(np.asarray(fn([nimage])))
Image.fromarray(np.uint8(mask/11.*255)).save('recog.png')
mask[mask != obj] = 1
mask[mask == obj] = 1
print mask
Image.fromarray(np.uint8(mask/11.*255)).save('mask.png')
masks = np.zeros([1,input_shape[0], input_shape[1], 12])
masks[:,:,:,obj] = mask
signal = tf.multiply(logits, masks)
loss = tf.reduce_mean(signal)
#loss = tf.reduce_sum((prob-masks)**2)
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
print weights.shape
weights_sorted = np.sort(weights)[::-1]
percentage_pre = (weights_sorted - np.min(weights_sorted))/np.ptp(weights_sorted)
percentage = percentage_pre/np.sum(percentage_pre)
print percentage
#plt.plot(np.cumsum(percentage))
plt.plot(percentage)
plt.savefig("vised/savefig.png")

idxs = np.argsort(weights)[::-1]
print ','.join(map(str,idxs[0:10]))
idx = idxs[0]
idx = 137
layer = np.asarray(layer)
channel = np.squeeze(layer[:,:,idx])
channel = (channel - np.min(channel, axis=(0, 1)))/np.ptp(channel)*255
cam_heatmap = cv2.resize(cv2.applyColorMap(np.uint8(channel), cv2.COLORMAP_JET), (input_shape[1], input_shape[0]))
cc = cam_heatmap*0.5+cvimg+0.5
cc = np.float32(cc)/np.max(cc,axis=(0,1,2))*255
cv2.imwrite('vised/{}_{}_heatmap.png'.format(name,idx),np.uint8(cc))
print idx, name

def get_img(idx, name):
    img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, max_iter=600, act_max_weight=300.,tv_weight=0.01,lp_norm_weight=10, input_modifiers=[Jitter(4)], verbose=True)
    #seed = visualize_activation_tf(inputs, end_points, name, filter_indices=idx,tv_weight=0.,act_max_weight=100., input_modifiers=[Jitter(0.05)],verbose=True)
    #img = visualize_activation_tf(inputs, end_points, name, filter_indices=idx,seed_input=seed,tv_weight=5., act_max_weight=15.,input_modifiers=[Jitter(0.05)], verbose=True)
    return img
img = get_img(idx, name)
Image.fromarray(np.uint8(img)).save('vised/{}_{}.png'.format(name,idx))
print idx, name

 
