# -*- coding: UTF-8 -*-
import numpy as np
import cv2
from tkinter import *
#import threading
from gtts import gTTS
import os


# 子執行緒的工作函數
def job(name):
    cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite( './faces/' + name + '.jpg',frame)
            #tts=gTTS(text='生日快樂', lang='zh-tw')
            #tts=gTTS(text='ありがとう', lang='ja')
            tts=gTTS(text=name, lang='en')
            tts.save("./sounds/" + name + ".mp3")
            os.system("mpg321 " + "./sounds/" + name + ".mp3")
            break
    # When everything done, release the captur
    cap.release()
    cv2.destroyAllWindows()


master = Tk()
master.title('登錄')
Label(master, text="名字").grid(row=0)
#Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
#e2 = Entry(master)
e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
Button(master, text='離開', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='確定', command=(lambda : job(e1.get()))).grid(row=3, column=1, sticky=W, pady=4)

#t=threading.Thread(target = job)
#t.start()


mainloop( )



