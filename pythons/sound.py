# -*- coding: UTF-8 -*-

from pygame import mixer # Load the required library
import time

mixer.init()
mixer.music.load('歐巴馬.mp3')
mixer.music.play()
time.sleep(2)
