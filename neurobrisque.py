# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:44:51 2019

@author: Francois
"""

import math
import numpy as np
import os
import skimage
import cv2
from PIL import Image
from math import sqrt

from skimage.viewer import ImageViewer
from skimage.color import rgb2gray
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#img=mpimg.imread(impath)
#imgplot = plt.imshow(img)
#plt.show()

#def gray_scale(image,output='array'):
#    pixels = image.load() # create the pixel map
#
#    for x in range(image.size[0]): # for every pixel:
#        for y in range(image.size[1]):
#            pixels[x,y] = (red,green,blue)
#                # change to black if not red
#            pixels[x,y] = (0, 0 ,0)
#            intensity = (red*0.2126+green*0.7152+blue*0.0722)
#    grayscaleArray = np.array(image)
#
#            pixValues = image.getpixel((x,y))
#            red,green,blue = pixValues
#            grayscaleArray[y,x].reshape((1,1))
#            grayscaleArray[y,x] = intensity
#    if output == 'image':
#        grayscaleArray = Image.fromarray(grayscaleArray,mode='L')
#    return grayscaleArray
def gray_scale(image,output='array'):
    width,heigth = image.size
    grayscaleArray = np.array(image)
    for x in range(width):
        for y in range(heigth):
            pixValues = image.getpixel((x,y))
            red,green,blue = pixValues
            intensity = [red*0.2126+green*0.7152+blue*0.0722]
            grayscaleArray[y,x].reshape(-1)
            grayscaleArray[y,x] = intensity
    if output == 'image':
        grayscaleArray = Image.fromarray(grayscaleArray)
    return grayscaleArray
impath = "C:/Users/Francois/GitHub/ImageTask/500_clothing/500_clothing_camisole/500_camisole01.jpeg"
image = Image.open(impath)
imGS = image.convert(mode='L')
grayscaleIm = gray_scale(image,output='image')

def gaussian_blur(image,output='array'):
    grayscaleIm = gray_scale(image,output='image')
    localmeanfield = np.array(grayscaleIm)
    width,heigth = grayscaleIm.size
                                  # Get mean and standard deviation
    stdev = np.std(localmeanfield)
    variance = math.pow(stdev,2)
    for x in range(width):
        for y in range(heigth):
            pixVal = grayscaleIm.getpixel((x,y))[0]
            coefficient = math.pow(math.e,-1*math.pow(pixVal,2)/2*variance)
            gaussblur = (1/math.sqrt(2*math.pi*variance))*coefficient
            localmeanfield[y,x] = gaussblur
    if output == 'image':
        localmeanfield = Image.fromarray(localmeanfield)
    return localmeanfield
    
def neuromodBRISQUE(impath):
    image = Image.open(impath)
    grayscaleIm = gray_scale(image,output='image')
    localmeanfieldFRANK = gaussian_blur(grayscaleIm)
    localvariancefieldFRANK = gaussian_blur(localmeanfieldFRANK,output='image')
    width,heigth = image.size
    im_MSCN = np.array(grayscaleIm)
    for x in range(width):
        for y in range(heigth):
            intensity = grayscaleIm.getpixel((x,y))[0]
            lmf = localmeanfieldFRANK.getpixel((x,y))[0]
            lvf = localvariancefieldFRANK.getpixel((x,y))[0]
            MSCN = (intensity-lmf)/(lvf+1)
            im_MSCN[y,x] = MSCN
    return im_MSCN
    
    
        
        
#        sigma = skimage.filters.gaussian(mu,3)
#        newIm = im_io
#        newIm[pixel] = intensity

##    grayscale = rgb2gray(im_io)

impath = "C:/Users/Francois/GitHub/ImageTask/500_clothing/500_clothing_camisole/500_camisole01.jpeg"
image = Image.open(impath)
grayscaleIm = gray_scale(image,output='image')
localmeanfield = gaussian_blur(image)
im_MSCN = neuromodBRISQUE(impath)
f, axarr = plt.subplots(1,3,figsize=(12,6))
axarr[0].imshow(image)
axarr[1].imshow(grayscaleIm)
axarr[2].imshow(imGS)
#axarr[3].imshow(im_MSCN)
#brisque = neuromodBRISQUE(impath)
#newImPlot = plt.imshow(newIm)      
#    im_io_plt = plt.imshow(im_io)
#    im_ioGS = skimage.io.imread(impath,as_gray=True)
#    im_ioGS2 = rgb2gray(im_io)
#    sk2mpl = mpimg.imread(im_ioGS)
#    im_mp = mpimg.imread(impath)
#    implot = plt.imshow(im_ioGS)
#    plt.show(implot)
#    gaussBlur = skimage.filters.gaussian(im_io)
#    GSgaussBlur = skimage.filters.gaussian(grayscale,3)
#    gaussplot = plt.imshow(gaussBlur)
#    plt.show(gaussBlur)
#    
#    imGS= cv2.imread(impath, 1)
#    imRGB= cv2.imread(impath, 0)
#    imArray = np.array(im)
#    im= cv2.imread(impath)
#    #Convert the image te RGB if it is a .gif for example
#    image = image.convert ('RGB')
#    
#    width,length = image.size
#    nPixels = width*length
#    RGBvalues = []
#    for M in range(width):
#        for N in range(length):
#           pixelRGB = image.getpixel((M,N))
#           R,G,B = pixelRGB
#           intensity = sum(R*0.2126,G*0.7152,B*0.0722)
#           localMeanField = R+G+B
#           RGBvalues.append(pixelRGB)
#    return RGBvalues
#imageRGB = image.convert('RGB')
#imMatrix = np.array(image)
#blurred = cv2.GaussianBlur(imageRGB, (0,0), 1.166)
#mscn = MSCN(image)         
#           luminance = 0.3*R + 0.59*G + 0.11*B
#           brightness = sum([R,G,B])/3
#           sigma = (luminance-brigthness)**2
#           
#    #coordinates of the pixel
#    X,Y = 0,0
#    #Get RGB
#def gaussBlur(image):

# how to compare 2 images:
#        fig, axes = plt.subplots(1, 2, figsize=(12, 6),sharex=True)
#        ax = axes.ravel()
#        ax[0].imshow(localmeanfield)
#        ax[0].set_title("francois")
#        ax[1].imshow(mu)
#        ax[1].set_title("skimage")
#        fig.tight_layout()
#        plt.show()