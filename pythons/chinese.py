# -*- coding: utf-8 -*-
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont
 
if __name__ == '__main__':
 
    img_OpenCV = cv2.imread('test.jpg')
    # 图像从OpenCV格式转换成PIL格式
    img_PIL = Image.fromarray(cv2.cvtColor(img_OpenCV, cv2.COLOR_BGR2RGB))
 
    # 字体  字体*.ttc的存放路径一般是： /usr/share/fonts/opentype/noto/ 查找指令locate *.ttc
    font = ImageFont.truetype('WCL-06.ttf', 40)
    # 字体颜色
    fillColor = (255,0,0)
    # 文字输出位置
    position = (100,100)
    # 输出内容
    str = '在圖片上秀出中文'
 
    # 需要先把输出的中文字符转换成Unicode编码形式
    if not isinstance(str, unicode):
        str = str.decode('utf8')
 
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, str, font=font, fill=fillColor)
    # 使用PIL中的save方法保存图片到本地
    # img_PIL.save('02.jpg', 'jpeg')
 
    # 转换回OpenCV格式
    img_OpenCV = cv2.cvtColor(numpy.asarray(img_PIL),cv2.COLOR_RGB2BGR)
    cv2.imshow("print chinese to image",img_OpenCV)
    cv2.waitKey()
    cv2.imwrite('03.jpg',img_OpenCV)
 
