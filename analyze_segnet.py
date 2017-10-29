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
sess = tf.Session()
saver = tf.train.Saver()
saver.restore(sess,'weights/segnet_tf.ckpt')
K.set_session(sess)
K.manual_variable_initialization(True)
nimage = np.asarray([Image.open('ouzel.jpg').resize(input_shape).getdata()]).astype(np.float32)
nimage = np.reshape(nimage,(input_shape[0],input_shape[1],3))
nimage = np.expand_dims(nimage,0 )
fn = K.function([inputs], [logits])
a = fn([nimage])

#visualize filters
name = 'conv1_1_D'
name = 'conv4_2_bn'
name = 'relu_2'
name = 'conv4_2'
name = 'conv3_1_D'
name = 'relu5_3'
idx =8
#img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, tv_weight=.0,lp_norm_weight=0., input_modifiers=[Jitter(0.05)])
#img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, max_iter=1800, act_max_weight=0.1,tv_weight=0.01,lp_norm_weight=10000, input_modifiers=[Jitter(16)], verbose=True)
img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, tv_weight=.0,lp_norm_weight=0., input_modifiers=[Jitter(0.05)])
img = visualize_activation_tf(inputs,end_points,name, filter_indices=idx, max_iter=800, act_max_weight=1.,tv_weight=0.01,lp_norm_weight=100, input_modifiers=[Jitter(16)], verbose=True)
Image.fromarray(np.uint8(img)).save('{}_{}.png'.format(name,idx))

nimage = np.asarray([Image.open('test.png').resize(input_shape).getdata()]).astype(np.float32)
nimage2 = nimage
nimage = np.reshape(nimage,(input_shape[0],input_shape[1],3))
nimage = cv2.resize(cv2.imread('test.png'), (input_shape[1], input_shape[0]))

nimage = np.expand_dims(nimage,0 )
K.set_session(sess)
K.manual_variable_initialization(True)
outputs = tf.argmax(logits, axis=3)
fn=K.function([inputs],[outputs])
seged=fn([nimage])
seged = np.asarray(seged)
seged = np.squeeze(seged)
cv2.imwrite('recog.png',np.uint8(seged/11.0*255))
 
