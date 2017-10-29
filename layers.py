import numpy as np

import tensorflow as tf

from tensorflow.python.ops import gen_nn_ops
from tensorflow.python.framework import ops


def unpool_with_argmax(pool, ind, name = None, ksize=[1, 2, 2, 1], upsample=[-1,-1]):

    """
       Unpooling layer after max_pool_with_argmax.
       Args:
           pool:   max pooled output tensor
           ind:      argmax indices
           ksize:     ksize is the same as for the pool
       Return:
           unpool:    unpooling tensor

    """
    upsample_w = upsample[0]
    upsample_h = upsample[1]
    with tf.variable_scope(name):
        input_shape = pool.get_shape().as_list()
        if (upsample_h > 0 or upsample_w > 0):
            output_shape = (input_shape[0],upsample_h,upsample_w, input_shape[3])
        else:
            output_shape = (input_shape[0], input_shape[1] * ksize[1], input_shape[2] * ksize[2], input_shape[3])


        flat_input_size = np.prod(input_shape)
        flat_output_shape = [output_shape[0], output_shape[1] * output_shape[2] * output_shape[3]]

        pool_ = tf.reshape(pool, [flat_input_size])
        batch_range = tf.reshape(tf.range(output_shape[0], dtype=ind.dtype), shape=[input_shape[0], 1, 1, 1])
        b = tf.ones_like(ind) * batch_range
        b = tf.reshape(b, [flat_input_size, 1])
        ind_ = tf.reshape(ind, [flat_input_size, 1])
        ind_ = tf.concat([b, ind_], 1)

        ret = tf.scatter_nd(ind_, pool_, shape=flat_output_shape)
        ret = tf.reshape(ret, output_shape)
        return ret

"""
@ops.RegisterGradient("MaxPoolWithArgmax")
def _MaxPoolGradWithArgmax(op, grad, unused_argmax_grad):
    return gen_nn_ops._max_pool_grad_with_argmax(op.inputs[0],
                                                 grad,
                                                 op.outputs[1],
                                                 op.get_attr("ksize"),
                                                 op.get_attr("strides"),
                                                 padding=op.get_attr("padding"))
"""

DEFAULT_PADDING = 'SAME'
trainable = True

def make_var(name, shape):
    '''Creates a new TensorFlow variable.'''
    return tf.get_variable(name, shape, trainable)

def validate_padding(padding):
    '''Verifies that the padding is one of the supported ones.'''
    assert padding in ('SAME', 'VALID')

def conv(input,
         k_h,
         k_w,
         c_o,
         s_h,
         s_w,
         name,
         relu=True,
         padding=DEFAULT_PADDING,
         group=1,
         biased=True):
    # Verify that the padding is acceptable
    validate_padding(padding)
    # Get the number of channels in the input
    c_i = input.get_shape()[-1]
    # Verify that the grouping parameter is valid
    assert c_i % group == 0
    assert c_o % group == 0
    # Convolution for a given input and kernel
    convolve = lambda i, k: tf.nn.conv2d(i, k, [1, s_h, s_w, 1], padding=padding)
    with tf.variable_scope(name) as scope:
        kernel = make_var('weights', shape=[k_h, k_w, c_i / group, c_o])
        if group == 1:
            # This is the common-case. Convolve the input without any further complications.
            output = convolve(input, kernel)
        else:
            # Split the input into groups and then convolve each of them independently
            input_groups = tf.split(3, group, input)
            kernel_groups = tf.split(3, group, kernel)
            output_groups = [convolve(i, k) for i, k in zip(input_groups, kernel_groups)]
            # Concatenate the groups
            output = tf.concat(3, output_groups)
        # Add the biases
        if biased:
            biases = make_var('biases', [c_o])
            output = tf.nn.bias_add(output, biases)
        if relu:
            # ReLU non-linearity
            output = tf.nn.relu(output, name=scope.name)
        return output

def relu(input, name):
    return tf.nn.relu(input, name=name)

def max_pool(input, k_h, k_w, s_h, s_w, name, padding=DEFAULT_PADDING):
    validate_padding(padding)
    return tf.nn.max_pool(input,
                          ksize=[1, k_h, k_w, 1],
                          strides=[1, s_h, s_w, 1],
                          padding=padding,
                          name=name)
def batch_normalization(input, name, scale_offset=True, relu=False):
    # NOTE: Currently, only inference is supported
    with tf.variable_scope(name) as scope:
        shape = [input.get_shape()[-1]]
        if scale_offset:
            scale = make_var('mean', shape=shape)
            offset = make_var('variance', shape=shape)
        else:
            scale, offset = (None, None)
        output = tf.nn.batch_normalization(
            input,
            #mean=make_var('mean', shape=shape),
            #variance=make_var('variance', shape=shape),
            mean=0.0,
            variance=1.0,
            offset=offset,
            scale=scale,
            # TODO: This is the default Caffe batch norm eps
            # Get the actual eps from parameters
            variance_epsilon=1e-5,
            name=name)
        if relu:
            output = tf.nn.relu(output)
        return output
 
