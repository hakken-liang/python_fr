# -*- coding: UTF-8 -*-
import face_recognition
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy
from pygame import mixer # Load the required library
import time
import threading
import os
from gtts import gTTS
import os


files = os.listdir("./faces");

#print(files)

knowns = []
for f in files:
    #print(f.split('.')[0])
    if f.split('.')[1] == 'jpg':
        knowns.append(f.split('.')[0])
print(knowns)


# 子執行緒的工作函數
def job(name):
    mixer.music.load(name + '.mp3')
    mixer.music.play()
    time.sleep(2)

video_capture = cv2.VideoCapture(0)


knowns_encodings = []
for n in knowns:
    knowns_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file( "./faces/" + n + ".jpg"))[0])

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


 # 字体  字体*.ttc的存放路径一般是： /usr/share/fonts/opentype/noto/ 查找指令locate *.ttc
font = ImageFont.truetype('./fonts/WCL-06.ttf', 40)

# 字体颜色
fillColor = (255,0,0)
mixer.init()
#threads_pool = set()

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(knowns_encodings, face_encoding, 0.4)
            name = "不知是誰"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = knowns[first_match_index]
                #mixer.music.load(name + '.mp3')
                #mixer.music.play()
                #time.sleep(2)
                #job(name)
                #t=threading.Thread(target = job, args = (name,))
                #t.start()
                #threads_pool.add(threading.Thread(target = job, args = (name,)))
                '''
                for t in threads_pool:
                    if not t.isAlive():
                        t.start()
                '''
            face_names.append(name)
            print(face_names)
            for n in knowns:
                if cv2.waitKey(10) & 0xFF == ord('w'):
                    t=threading.Thread(target = (lambda : os.system("mpg321 " + "./sounds/" + name + ".mp3")))
                    t.start()
    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #font = cv2.FONT_HERSHEY_DUPLEX
        #cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # 图像从OpenCV格式转换成PIL格式
        img_PIL = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
 
   
        # 文字输出位置
        position = (left,bottom)
        # 输出内容
        str = name
 
        # 需要先把输出的中文字符转换成Unicode编码形式
        #if not isinstance(str, unicode):
            #str = str.decode('utf8')
 
        draw = ImageDraw.Draw(img_PIL)
        draw.text(position, str, font=font, fill=fillColor)
        # 使用PIL中的save方法保存图片到本地
        # img_PIL.save('02.jpg', 'jpeg')
 
        # 转换回OpenCV格式
        frame = cv2.cvtColor(numpy.asarray(img_PIL),cv2.COLOR_RGB2BGR)

    # Display the resulting image
    cv2.imshow("FACE", frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
