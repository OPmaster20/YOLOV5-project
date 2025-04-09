import cv2 as cv
import random
import numpy as np

#30 / 3 = 6
precentage = 0
filepath = ""
savepath = ""
def Quantitymeasurement(n = 0,effect = 0):
    global precentage
    precentage = int(n / effect)

def main(p = 0):
    global precentage
    if p == 1:
        AddErosion(precentage)
    elif p == 2:
        AddSmooth(precentage)
    elif p == 3:
        AddLinear(precentage)
    elif p == 4:
        AddExpansion(precentage)
    else:
        Addtransformations(precentage)

def AddSmooth(number = 0):
    global filepath, savepath
    imgs = cv.imread(filepath)
    name = savepath + "Smooth_"
    for i in range(number):
        element = random.randint(1,100)
        tuf = random.randint(1, 10)
        if element % 2 == 0:
            element = element + 1

        if tuf % 2 == 0:
            smooth_imgs = cv.GaussianBlur(imgs,(element,element),0)
            cv.imwrite((name + str(i + 1) + ".jpg"), smooth_imgs)
        else:
            if element == 1:
                element = 3
            median_imgs = cv.medianBlur(imgs,element)
            cv.imwrite((name + str(i + 1) + ".jpg"), median_imgs)



def AddLinear(number = 0):
    global filepath, savepath
    imgs = cv.imread(filepath)
    name = savepath + "Linear_"
    for i in range(number):
        k = random.randint(1,50)
        kernel = np.ones((k, k)) / 100
        linear_imgs = cv.filter2D(imgs,-1,kernel)
        cv.imwrite((name + str(i + 1) + ".jpg"), linear_imgs)

def AddExpansion(number = 0):
    global filepath, savepath
    imgs = cv.imread(filepath)
    name = savepath + "Expansion_"
    for i in range(number):
        unit = random.randint(1,100)
        k = np.ones((unit, unit), np.uint8)
        dilation_imgs = cv.dilate(imgs, k, iterations=1)
        cv.imwrite((name + str(i + 1) + ".jpg"), dilation_imgs)



def Addtransformations(number = 0):
    global filepath, savepath
    imgs = cv.imread(filepath)
    name = savepath + "transformation_"
    h,w,c = imgs.shape
    for i in range(number):
        degree = random.randint(1,170)
        rotate = cv.getRotationMatrix2D((int(h/2),int(w/2)), degree, 1.0)
        rotate_imgs = cv.warpAffine(imgs,rotate,(h,w))
        cv.imwrite((name + str(i + 1) + ".jpg"), rotate_imgs)

def AddErosion(number = 0):
    global filepath,savepath
    imgs = cv.imread(filepath)
    name = savepath + "erosion_"
    for i in range(number):
        element = random.randint(1,50)
        val = np.ones((element,element),np.uint8)
        erosion_imgs = cv.erode(imgs,val,iterations=1)
        cv.imwrite((name + str(i + 1) + ".jpg"),erosion_imgs)



