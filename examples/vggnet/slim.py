import numpy as np
from tensorflow.contrib.keras import backend as K
from PIL import Image
from vis.utils import utils
from tensorflow.contrib.keras import activations
from tensorflow.contrib.keras.python.keras.models import load_model
from tensorflow.contrib.keras.python.keras.layers.core import Activation
from tensorflow.contrib.keras.python.keras.models import Sequential, Model
from tensorflow.contrib.keras.python.keras.layers import InputLayer, Input, Dense
from vis.visualization import visualize_activation
from vis.input_modifiers import Jitter
import sys, os
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.python.slim.nets.vgg as vgg
import tensorflow as tf
import vgg_preprocessing

image_size = vgg.vgg_16.default_image_size
print image_size
inp = tf.placeholder("float", shape=[None, image_size, image_size,3])
graph=tf.Graph()
graph.as_default()

inputs=Input(shape=(image_size, image_size, 3,))
with slim.arg_scope(vgg.vgg_arg_scope()):
    vgg_output, check_points = vgg.vgg_16(inputs, num_classes=1000, is_training=False)
init_fn = slim.assign_from_checkpoint_fn('examples/vggnet/vgg_16.ckpt', slim.get_model_variables('vgg_16'))
#model.add(InputLayer(input_tensor=output, input_shape=(None, 1000)))
outputs=Dense(100)(vgg_output)
#outputs=Activation('softmax')(outputs)
model = Model(inputs=inputs, outputs=outputs)
sess= tf.Session()
K.set_session(sess)
init_fn(sess)
#image = tf.cast(tf.image.decode_png(tf.read_file('../test.png'), channels=3),tf.int32)
image=np.expand_dims(Image.open('ouzel.jpg').resize((image_size,image_size)),axis=0)
#image = tf.image.decode_jpeg(tf.read_file('../test.png'), channels=3)
#vgg_mean = np.array([123.68, 116.779, 103.939], dtype=np.float32).reshape((1,1,3)) # This one for Tensorflow
"""
def vgg_preprocess(x):
    x = x - vgg_mean
    return x[:,:,::-1] # reverse axis rgb->bgr # This one for Tensorflow (channels last))])))])
"""
#processed_image = vgg_preprocessing.preprocess_imagv(image, image_size, image_size, is_training=False)
#processed_image = vgg_preprocess(image)
#processed_images  = tf.expand_dims(processed_image,0 )
#y = model.predict(processed_images,batch_size=1)
#processed_images  = tf.expand_dims(image,0 )
#K.set_learning_phase(0)
#fnk = K.function([model.input],[ output])
print model
#y = fn(processed_images)
y = model([image])
#print np.argmax(np.asarray(y))
print model.summary()
