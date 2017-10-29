import numpy as np
from tensorflow.contrib.keras import backend as K
from PIL import Image
from vis.utils import utils
from tensorflow.contrib.keras import activations
from tensorflow.contrib.keras.python.keras.models import load_model
from tensorflow.contrib.keras.python.keras.layers.core import Activation
from tensorflow.contrib.keras.python.keras.models import Sequential
from tensorflow.contrib.keras.python.keras.layers import InputLayer
from vis.visualization import visualize_activation
from vis.input_modifiers import Jitter
import sys, os
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.python.slim.nets.vgg as vgg
import tensorflow as tf
image_size = vgg.vgg_16.default_image_size


print image_size
inp = tf.placeholder("float", shape=[None, image_size, image_size,3])
with slim.arg_scope(vgg.vgg_arg_scope()):
    output, end_points = vgg.vgg_16(inp, num_classes=1000, is_training=False)
prob = tf.nn.softmax(output)

sess = tf.Session()
saver = tf.train.Saver()
saver.restore(sess, 'examples/vggnet/vgg_16.ckpt')
nimage = np.asarray([Image.open('ouzel.jpg').resize((224,224)).getdata()]).astype(np.float32)
nimage = np.reshape(nimage,(224,224,3))
nimage = np.expand_dims(nimage,0 )
K.set_session(sess)
K.manual_variable_initialization(True)
fn=K.function([inp],[prob])
prob2=fn([nimage])
print np.asarray(prob2).shape
print np.argmax(np.asarray(prob2))
print end_points['vgg_16/conv1/conv1_2']
