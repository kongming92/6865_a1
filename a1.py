#a1.py
#Assignment 1 (or 0, depending on who asks)
#by Abe Davis
#
#You can change the 'as' calls below if you want to call functions differently (i.e. numpy.function() instead of np.function())

import imageIO as io
import numpy as np
import scipy as sp

def brightness(im, factor):
    imb = im.copy()
    return np.clip(imb * factor, 0, 1)


def contrast(im, factor, midpoint=0.3):
    imc = im.copy()
    return np.clip((imc - midpoint) * factor + midpoint, 0, 1)


def frame(im):
    imf = im.copy()
    (height, width, rgb) = np.shape(imf)
    imf[:, 0] = 0
    imf[0, :] = 0
    imf[:, width - 1] = 0
    imf[height - 1, :] = 0
    return imf


def BW(im, weights=[0.3,0.6,0.1]):
    img = im.copy()
    (height, width, rgb) = np.shape(img)
    for y in xrange(height):
        for x in xrange(width):
            img[y][x] = np.dot(img[y][x], weights)
    return img


def lumiChromi(im):
    imcopy = im.copy()
    bw = BW(imcopy)
    return (bw, imcopy / bw)


def brightnessContrastLumi(im, brightF, contrastF, midpoint=0.3):
    outim = im.copy()
    imL, imC = lumiChromi(outim)
    return contrast(brightness(imL, brightF), contrastF, midpoint) * imC


def rgb2yuv(im):
    imyuv = im.copy()
    M = np.array([[0.299, 0.587, 0.114], [-0.14713, -0.28886, 0.436], [0.615, -0.51499, -0.1001]])
    (height, width, rgb) = np.shape(imyuv)
    for y in xrange(height):
        for x in xrange(width):
            imyuv[y][x] = np.dot(M, imyuv[y][x])
    return imyuv


def yuv2rgb(im):
    imrgb = im.copy()
    M = np.matrix([[1, 0, 1.13983], [1, -0.39465, -0.58060], [1, 2.03211, 0]])
    (height, width, yuv) = np.shape(imrgb)
    for y in xrange(height):
        for x in xrange(width):
            imrgb[y][x] = np.dot(M, imrgb[y][x])
    return imrgb


def saturate(im, k):
    imyuv = rgb2yuv(im.copy())
    return yuv2rgb(imyuv * [1, k, k])


#spanish castle URL: http://www.johnsadowski.com/big_spanish_castle.php
#HINT: to invert color for a YUV image, negate U and V
def spanish(im):
    imyuv = rgb2yuv(im)
    imyuv[:, :, 0] = 0.2    # constant luminance
    imC = yuv2rgb(imyuv * [1, -1, -1])
    imL = yuv2rgb(rgb2yuv(im) * [1, 0, 0])

    (height, width, rbg) = np.shape(im)
    imC[height/2, width/2] = 0
    imL[height/2, width/2] = 0
    return (imL, imC)


def histogram(im, N):
    hist = [0] * N
    imc = BW(im)
    (height, width, c) = np.shape(imc)
    for y in xrange(height):
        for x in xrange(width):
            luminance = imc[y, x, 0]
            bin = int(luminance * N)
            if bin > N-1:
                bin = N-1
            elif bin < 0:
                bin = 0
            hist[bin] += 1
    return np.array([float(bin) / sum(hist) for bin in hist])


def printHisto(im, N, scale):
    hist = histogram(im, N)
    for bin in hist:
       print 'X' * int(bin * N * scale)
