#from tensorflow.contrib.keras.applications import VGG16
import numpy as np
from vis.visualization import visualize_activation_tf
from vis.input_modifiers import Jitter
from tensorflow.contrib.keras import backend as K
from PIL import Image
from vis.utils import utils
from vis.visualization import visualize_activation
from vis.input_modifiers import Jitter
import sys, os
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.python.slim.nets.vgg as vgg
import tensorflow as tf
 
image_size = vgg.vgg_16.default_image_size
inp = tf.placeholder("float", shape=[None, image_size, image_size,3])
with slim.arg_scope(vgg.vgg_arg_scope()):
    output, end_points = vgg.vgg_16(inp, num_classes=1000, is_training=False)
prob = tf.nn.softmax(output)
sess = tf.Session()
saver = tf.train.Saver()
saver.restore(sess, 'examples/vggnet/vgg_16.ckpt')
"""
nimage = np.asarray([Image.open('ouzel.jpg').resize((224,224)).getdata()]).astype(np.float32)
nimage = np.reshape(nimage,(224,224,3))
nimage = np.expand_dims(nimage,0 )
"""
K.set_session(sess)
K.manual_variable_initialization(True)

idx=30
#seed = visualize_activation(model, layer_idx, filter_indices=idx,tv_weight=0., input_modifiers=[Jitter(0.05)])
#img = visualize_activation(model, layer_idx, filter_indices=idx,seed_input=seed,  input_modifiers=[Jitter(0.05)])
#img = visualize_activation(model, layer_idx,max_iter=500, filter_indices=idx, input_modifiers=[Jitter(0.05)])
img = visualize_activation_tf(inp,end_points,'vgg_16/conv1/conv1_2',max_iter=200, filter_indices=idx, input_modifiers=[Jitter(16)])
Image.fromarray(np.uint8(img)).save('am2.png')
#img = visualize_activation(model, layer_idx, filter_indices=20, max_iter=500, input_modifiers=[Jitter(16)])

