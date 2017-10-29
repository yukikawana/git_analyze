from layers import conv, batch_normalization, relu, unpool_with_argmax
import tensorflow as tf
def segnet(inputs):
    end_points = {}
    net = conv(inputs,3, 3, 64, 1, 1, relu=False, name='conv1_1')
    end_points['conv1_1'] = net
    net = batch_normalization(net,scale_offset=True, name='conv1_1_bn')
    end_points['conv1_1_bn'] = net
    net = relu(net,name='relu1_1')
    end_points['relu1_1'] = net
    net = conv(net,3, 3, 64, 1, 1, relu=False, name='conv1_2')
    end_points['conv1_2'] = net
    net = batch_normalization(net,scale_offset=True, name='conv1_2_bn')
    end_points['conv1_2_bn'] = net
    net = relu(net,name='relu1_2')
    end_points['relu1_2'] = net
    net, arg1 = tf.nn.max_pool_with_argmax(net, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name='pool1')
    end_points['pool1'] = net
    net = conv(net,3, 3, 128, 1, 1, relu=False, name='conv2_1')
    end_points['conv2_1'] = net
    net = batch_normalization(net,scale_offset=True, name='conv2_1_bn')
    end_points['conv2_1_bn'] = net
    net = relu(net,name='relu2_1')
    end_points['relu2_1'] = net
    net = conv(net,3, 3, 128, 1, 1, relu=False, name='conv2_2')
    end_points['conv2_2'] = net
    net = batch_normalization(net,scale_offset=True, name='conv2_2_bn')
    end_points['conv2_2_bn'] = net
    net = relu(net,name='relu2_2')
    end_points['relu2_2'] = net
    net, arg2 = tf.nn.max_pool_with_argmax(net, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name='pool2')
    end_points['pool2'] = net
    net = conv(net,3, 3, 256, 1, 1, relu=False, name='conv3_1')
    end_points['conv3_1'] = net
    net = batch_normalization(net,scale_offset=True, name='conv3_1_bn')
    end_points['conv3_1_bn'] = net
    net = relu(net,name='relu3_1')
    end_points['relu3_1'] = net
    net = conv(net,3, 3, 256, 1, 1, relu=False, name='conv3_2')
    end_points['conv3_2'] = net
    net = batch_normalization(net,scale_offset=True, name='conv3_2_bn')
    end_points['conv3_2_bn'] = net
    net = relu(net,name='relu3_2')
    end_points['relu3_2'] = net
    net = conv(net,3, 3, 256, 1, 1, relu=False, name='conv3_3')
    end_points['conv3_3'] = net
    net = batch_normalization(net,scale_offset=True, name='conv3_3_bn')
    end_points['conv3_3_bn'] = net
    net = relu(net,name='relu3_3')
    end_points['relu3_3'] = net
    net, arg3 = tf.nn.max_pool_with_argmax(net, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name='pool3')
    end_points['pool3'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv4_1')
    end_points['conv4_1'] = net
    net = batch_normalization(net,scale_offset=True, name='conv4_1_bn')
    end_points['conv4_1_bn'] = net
    net = relu(net,name='relu4_1')
    end_points['relu4_1'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv4_2')
    end_points['conv4_2'] = net
    net = batch_normalization(net,scale_offset=True, name='conv4_2_bn')
    end_points['conv4_2_bn'] = net
    net = relu(net,name='relu4_2')
    end_points['relu4_2'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv4_3')
    end_points['conv4_3'] = net
    net = batch_normalization(net,scale_offset=True, name='conv4_3_bn')
    end_points['conv4_3_bn'] = net
    net = relu(net,name='relu4_3')
    end_points['relu4_3'] = net
    net, arg4 = tf.nn.max_pool_with_argmax(net, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name='pool4')
    end_points['pool4'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv5_1')
    end_points['conv5_1'] = net
    net = batch_normalization(net,scale_offset=True, name='conv5_1_bn')
    end_points['conv5_1_bn'] = net
    net = relu(net,name='relu5_1')
    end_points['relu5_1'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv5_2')
    end_points['conv5_2'] = net
    net = batch_normalization(net,scale_offset=True, name='conv5_2_bn')
    end_points['conv5_2_bn'] = net
    net = relu(net,name='relu5_2')
    end_points['relu5_2'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv5_3')
    end_points['conv5_3'] = net
    net = batch_normalization(net,scale_offset=True, name='conv5_3_bn')
    end_points['conv5_3_bn'] = net
    net = relu(net,name='relu5_3')
    end_points['relu5_3'] = net
    net, arg5 = tf.nn.max_pool_with_argmax(net, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name='pool5')
    end_points['pool5'] = net
    net = unpool_with_argmax(net, arg5, name='unpool5',upsample=[30,23])
    end_points['unpool5'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv5_3_D')
    end_points['conv5_3_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv5_3_D_bn')
    end_points['conv5_3_D_bn'] = net
    net = relu(net,name='relu5_3_D')
    end_points['relu5_3_D'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv5_2_D')
    end_points['conv5_2_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv5_2_D_bn')
    end_points['conv5_2_D_bn'] = net
    net = relu(net,name='relu5_2_D')
    end_points['relu5_2_D'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv5_1_D')
    end_points['conv5_1_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv5_1_D_bn')
    end_points['conv5_1_D_bn'] = net
    net = relu(net,name='relu5_1_D')
    end_points['relu5_1_D'] = net
    net = unpool_with_argmax(net, arg4, name='unpool4',upsample=[60,45])
    end_points['unpool4'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv4_3_D')
    end_points['conv4_3_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv4_3_D_bn')
    end_points['conv4_3_D_bn'] = net
    net = relu(net,name='relu4_3_D')
    end_points['relu4_3_D'] = net
    net = conv(net,3, 3, 512, 1, 1, relu=False, name='conv4_2_D')
    end_points['conv4_2_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv4_2_D_bn')
    end_points['conv4_2_D_bn'] = net
    net = relu(net,name='relu4_2_D')
    end_points['relu4_2_D'] = net
    net = conv(net,3, 3, 256, 1, 1, relu=False, name='conv4_1_D')
    end_points['conv4_1_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv4_1_D_bn')
    end_points['conv4_1_D_bn'] = net
    net = relu(net,name='relu4_1_D')
    end_points['relu4_1_D'] = net
    net = unpool_with_argmax(net, arg3, name='unpool3')
    end_points['unpool3'] = net
    net = conv(net,3, 3, 256, 1, 1, relu=False, name='conv3_3_D')
    end_points['conv3_3_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv3_3_D_bn')
    end_points['conv3_3_D_bn'] = net
    net = relu(net,name='relu3_3_D')
    end_points['relu3_3_D'] = net
    net = conv(net,3, 3, 256, 1, 1, relu=False, name='conv3_2_D')
    end_points['conv3_2_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv3_2_D_bn')
    end_points['conv3_2_D_bn'] = net
    net = relu(net,name='relu3_2_D')
    end_points['relu3_2_D'] = net
    net = conv(net,3, 3, 128, 1, 1, relu=False, name='conv3_1_D')
    end_points['conv3_1_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv3_1_D_bn')
    end_points['conv3_1_D_bn'] = net
    net = relu(net,name='relu3_1_D')
    end_points['relu3_1_D'] = net
    net = unpool_with_argmax(net, arg2, name='unpool2')
    end_points['unpool2'] = net
    net = conv(net,3, 3, 128, 1, 1, relu=False, name='conv2_2_D')
    end_points['conv2_2_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv2_2_D_bn')
    end_points['conv2_2_D_bn'] = net
    net = relu(net,name='relu2_2_D')
    end_points['relu2_2_D'] = net
    net = conv(net,3, 3, 64, 1, 1, relu=False, name='conv2_1_D')
    end_points['conv2_1_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv2_1_D_bn')
    end_points['conv2_1_D_bn'] = net
    net = relu(net,name='relu2_1_D')
    end_points['relu2_1_D'] = net
    net = unpool_with_argmax(net, arg1, name='unpool1')
    end_points['unpool1'] = net
    net = conv(net,3, 3, 64, 1, 1, relu=False, name='conv1_2_D')
    end_points['conv1_2_D'] = net
    net = batch_normalization(net,scale_offset=True, name='conv1_2_D_bn')
    end_points['conv1_2_D_bn'] = net
    net = relu(net,name='relu1_2_D')
    end_points['relu1_2_D'] = net
    net = conv(net,3, 3, 12, 1, 1, relu=False, name='conv1_1_D')
    end_points['conv1_1_D'] = net
    return net, end_points
