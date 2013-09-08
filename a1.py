#a1.py
#Assignment 1 (or 0, depending on who asks)
#by Abe Davis
#
#You can change the 'as' calls below if you want to call functions differently (i.e. numpy.function() instead of np.function())

import imageIO as io
import numpy as np
import scipy as sp

def brightness(im, factor):
    #imb = im.copy() #always work on a copy of th image!
    #modify brightness of image by factor
    #return imb


def contrast(im, factor, midpoint=0.3):
    #imc = im.copy()
    #modify contrast of image
    #return imc


def frame(im):
    #imf = im.copy()
    #apply frame to image
    #return imf


def BW(im, weights=[0.3,0.6,0.1]):
    #img = im.copy()
    #create black and white image
    #return img


def lumiChromi(im):
    #create lumi and chromi images. Remember to work on copies of im!
    #return (imL, imC)


def brightnessContrastLumi(im, brightF, contrastF, midpoint=0.3):
    #outim = im.copy()
    #modify brightness and contrast without changing the chrominance
    #return outim


def rgb2yuv(im):
    #imyuv = im.copy()
    #convert to yuv using the matrix given in the assignment handout
    #return imyuv


def yuv2rgb(im):
    #imrgb = im.copy()
    #convert to rgb using the matrix given in the assignment handout
    #return imrgb


def saturate(im, k):
    #create and return saturated image
    #return imS
    

#spanish castle URL: http://www.johnsadowski.com/big_spanish_castle.php
#HINT: to invert color for a YUV image, negate U and V
def spanish(im):
    #Create a pair of images for a spanish castle illusion
    #return (imL, imC)


def histogram(im, N):
    #create the histogram
    #return hist

def printHisto(im, N, scale):
    #print the histogram
        
        
