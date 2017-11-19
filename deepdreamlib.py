

# boilerplate code
#from __future__ import print_function
import numpy as np
import tensorflow as tf
import cv2


def showarray(a):
    a = np.uint8(np.clip(a, 0, 1)*255)
    return a
    


def tffunc(*argtypes):
    '''Helper that transforms TF-graph generating function into a regular one.
    See "resize" function below.
    '''
    placeholders = list(map(tf.placeholder, argtypes))
    def wrap(f):
        out = f(*placeholders)
        def wrapper(*args, **kw):
            #return out.eval(dict(zip(placeholders, args)), session=kw.get('sess'))
            #return out.eval(dict(zip(placeholders, args)), session=tf.Session())
            return out.eval(dict(zip(placeholders, args)), session=tf.get_default_session())
        return wrapper
    return wrap

# Helper function that uses TF to resize an image
def resize(img, size):
    """
    img = tf.expand_dims(img, 0)
    img = tf.image.resize_bilinear(img, size)[0,:,:,:]
    """
    img = cv2.resize(img, tuple(size[::-1]))
    return img
#resize = tffunc(np.float32, np.int32)(resize)




def calc_grad_tiled(img, t_grad,t_input, tile_size=512):
    '''Compute the value of tensor t_grad over the image in a tiled way.
    Random shifts are applied to the image to blur tile boundaries over 
    multiple iterations.'''
    input_shape = t_input.get_shape().as_list()[1:3]
    sz = tile_size
    h, w = img.shape[:2]
    sx, sy = np.random.randint(sz, size=2)
    img_shift = np.roll(np.roll(img, sx, 1), sy, 0)
    grad = np.zeros_like(img)
    for y in range(0, max(h-sz//2, sz),sz):
        for x in range(0, max(w-sz//2, sz),sz):
            sub = img_shift[y:y+sz,x:x+sz]
            sub = np.expand_dims(sub, 0)
            h_pad = input_shape[0] - h
            w_pad = input_shape[1] - w
            top = int(h_pad/2.)
            bottom = h_pad - top
            left = int(w_pad/2.)
            right = w_pad - left
            padding = [[0, 0], [top, bottom], [left, right], [0, 0]]
            sub = np.lib.pad(sub, padding, 'reflect')
            g = tf.get_default_session().run(t_grad, {t_input:sub})
            grad[y:y+sz,x:x+sz] = g[0,top:top+h, left:left+w, :]
    return np.roll(np.roll(grad, -sx, 1), -sy, 0)


# In[7]:


def render_deepdream(sess,input_tensor, grad, iter_n=10, step=1.5, octave_n=4, octave_scale=1.4, verbose=False):
    input_shape = input_tensor.get_shape().as_list()[1:3]
    img_noise = np.random.uniform(size=(input_shape[0],input_shape[1],3)) + 100.0
    print input_shape
    with sess.as_default():
        img = img_noise
        octaves = []
        for i in range(octave_n-1):
            hw = img.shape[:2]
            lo = resize(img, np.int32(np.float32(hw)/octave_scale))
            hi = img-resize(lo, hw)
            img = lo
            octaves.append(hi)
        
        # generate details octave by octave
        for octave in range(octave_n):
            if octave>0:
                hi = octaves[-octave]
                img = resize(img, hi.shape[:2])+hi
            for i in range(iter_n):
                if verbose:
                    print '{}th iter, in {} octave'.format(i,octave)
                g = calc_grad_tiled(img, grad, input_tensor)
                img += g*(step / (np.abs(g).mean()+1e-7))
    return showarray(img/255.0 )

