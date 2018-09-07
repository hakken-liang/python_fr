import numpy as np
import cv2 as cv

def zh_ch(string):    
    return string.encode("gbk").decode(errors="ignore")
img = np.zeros((512,512,3), np.uint8)
cv.imshow(zh_ch('图片'),img)
cv.waitKey(0)            
cv.destroyWindow('image') 