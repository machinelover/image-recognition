#-*- encoding:utf8 -*-
import cv2
import os
import sys
import random
# 获取分类器
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_dir = './my_faces'
if not os.path.exists(face_dir):
    os.makedirs(face_dir)
name=raw_input("please input your name:")
os.makedirs(face_dir+'/'+name)

# 打开摄像头 参数为输入流，可以为摄像头或视频文件
camera = cv2.VideoCapture(0)

# 改变亮度与对比度
def relight(img, alpha=1, bias=0):
    w = img.shape[1]
    h = img.shape[0]
    #image = []
    for i in range(0,w):
        for j in range(0,h):
            for c in range(3):
                tmp = int(img[j,i,c]*alpha + bias)
                if tmp > 255:
                    tmp = 255
                elif tmp < 0:
                    tmp = 0
                img[j,i,c] = tmp
    return img
i = 1
while 1:
    if (i <= 10000):
        print('It`s processing %s image.' % i)
        success, img = camera.read()        # 读帧
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转灰度图
        faces = classifier.detectMultiScale(gray_img, 1.3, 5)#用分类器获取脸部
        for f_x, f_y, f_w, f_h in faces:#截取原来图像的脸部
            face = img[f_y:f_y+f_h, f_x:f_x+f_w]
            face = cv2.resize(face, (128,128))
            face = relight(face, random.uniform(0.5, 1.5), random.randint(-50, 50))#重新调亮度
            cv2.imwrite(face_dir+'/'+name+'/'+str(i)+'.jpg', face)
            cv2.imshow('img',face)
            i+=1

        key = cv2.waitKey(10)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break
    else:
        break

