#!/usr/bin/python
import tensorflow as tf
from segnet import segnet
from keras import backend as K
from PIL import Image
import numpy as np
import pdb
import cv2


input_shape = (360, 480)
inputs = tf.placeholder(tf.float32, shape=(1, input_shape[0], input_shape[1], 3))
logits, end_points = segnet(inputs)
outputs = tf.argmax(logits, axis=3)
sess = tf.Session()
saver = tf.train.Saver()
saver.restore(sess,'weights/segnet_tf.ckpt')
nimage = np.asarray([Image.open('test.png').resize(input_shape).getdata()]).astype(np.float32)
nimage2 = nimage
nimage = np.reshape(nimage,(input_shape[0],input_shape[1],3))
nimage = cv2.resize(cv2.imread('test.png'), (input_shape[1], input_shape[0]))

nimage = np.expand_dims(nimage,0 )
K.set_session(sess)
K.manual_variable_initialization(True)
fn=K.function([inputs],[outputs])
seged=fn([nimage])
seged = np.asarray(seged)
seged = np.squeeze(seged)
cv2.imwrite('recog.png',np.uint8(seged/11.0*255))

