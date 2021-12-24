import cv2
import pyttsx3
from time import sleep

engine = pyttsx3.init()
cap = cv2.VideoCapture(0)
z = 1000
while z > -1000:
    while z > 0:
        success, img = cap.read()
        z = z-1
        sleep(1)
        gh = cv2.CascadeClassifier('frontface.xml')
        results = gh.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in results:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), thickness=2)
            cv2.imshow("Result", img)
            if x > 0:
                engine.say('Повернитесь боком')
                engine.runAndWait()
                z = 0

    if z == 0:
        while z > -1000:
            success, img = cap.read()
            z = z - 1
            gh = cv2.CascadeClassifier('profile.xml')
            results = gh.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)
            print(results)
            for (x, y, w, h) in results:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), thickness=2)
                cv2.imshow("Result", img)
                if x > 0:
                    engine.say('можете идти')
                    engine.runAndWait()
                    z = -1000
