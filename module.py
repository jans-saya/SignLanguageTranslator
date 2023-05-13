
import cv2
import mediapipe as mp
from gtts import gTTS
import os

drawingModule = mp.solutions.drawing_utils
handsModule = mp.solutions.hands

mod = handsModule.Hands()

h = 480
w = 640

def speak(a):
    tts = gTTS(text=a, lang='ru')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")


def findposition(frame):
    list=[]
    results = mod.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
       for handLandmarks in results.multi_hand_landmarks:
           drawingModule.draw_landmarks(frame, handLandmarks, handsModule.HAND_CONNECTIONS)
           list=[]
           for id, pt in enumerate (handLandmarks.landmark):
                x = int(pt.x * w)
                y = int(pt.y * h)
                list.append([id,x,y])

    return list            


def findnameoflandmark(frame):
     list=[]
     results = mod.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
     if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:


            for point in handsModule.HandLandmark:
                 list.append(str(point).replace ("< ","").replace("HandLandmark.", "").replace("_"," ").replace("[]",""))
     return list




