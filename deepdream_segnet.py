#!/usr/bin/python
import tensorflow as tf
from segnet import segnet
import numpy as np
from deepdreamlib import render_deepdream
import skimage.io
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
 #define input shape
channel = 229
channel = 20
channel = 138
channel = 163
channel = 357
channel = 69
channel = 434
channel = 250
name = 'conv5_3'
#name = 'conv1_1_D'
input_shape = (360, 480)

#construct graph
eval_graph = tf.Graph()
with eval_graph.as_default():
    inputs = tf.placeholder("float", shape=(1, input_shape[0],input_shape[1], 3))
    logits, end_points = segnet(inputs)
    #grad = tf.gradients(tf.reduce_max(end_points[name][:,:,:,channel]), inputs)[0]
    grad = tf.gradients(tf.reduce_mean(end_points[name][:,:,:,channel])+tf.reduce_max(logits[:,:,:,9]), inputs)[0]

    sess = tf.Session(graph=eval_graph)
    saver = tf.train.Saver()
    saver.restore(sess,'weights/segnet_tf.ckpt')
#imgs = render_deepdream(end_points['relu5_3'][:,:,:,386],inputs,  img_noise, sess)
#imgs = render_deepdream(end_points['conv4_1_D'][:,:,:,9],inputs,  img_noise, sess)
#imgs = render_deepdream(end_points['conv5_3'][:,:,:,417],inputs,  img_noise, sess)
img = render_deepdream(sess, inputs, grad, iter_n=10, octave_n=10, verbose=True)
skimage.io.imsave('0.png',img)
