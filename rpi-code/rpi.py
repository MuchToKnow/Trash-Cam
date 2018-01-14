import requests
import base64
from cv2 import *
import json
import RPi.GPIO as GPIO
import time
import sys


img_path = "im2.jpg"
url = "http://35.163.191.108:3000/api/request"

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)
    serv1 = GPIO.PWM(13, 50)
    GPIO.setup(11, GPIO.OUT)
    serv2 = GPIO.PWM(11, 50)
    GPIO.setup(15, GPIO.OUT)
    serv3 = GPIO.PWM(15, 50)

    print("Starting img capture")
    cam = VideoCapture(0)
    if cam.isOpened():
        s, img = cam.read()
    else:
        print("Unable to open camera")
        clean_exit()
        sys.exit(1)
    cam.release()

    s, jimg = imencode(".jpeg", img)

    b64img = base64.b64encode(jimg)

    print("Sending POST")
    r = requests.post(url, json={"image" : b64img})

    jsresp = r.json()["status"]
    print(jsresp)


    serv1.start(12.5)
    serv2.start(12.5)
    serv3.start(12.5)

    # Compost
    if jsresp == 1:
        serv1.ChangeDutyCycle(2.5)
        time.sleep(8)
        serv1.ChangeDutyCycle(12.5)
    # Recycle
    elif jsresp == 2:
        serv2.ChangeDutyCycle(2.5)
        time.sleep(8)
        serv2.ChangeDutyCycle(12.5)
    # Trash
    elif jsresp == 3:
        serv3.ChangeDutyCycle(2.5)
        time.sleep(8)
        serv3.ChangeDutyCycle(12.5)
    # ALL
    else:
        serv1.ChangeDutyCycle(2.5)
        serv2.ChangeDutyCycle(2.5)
        serv3.ChangeDutyCycle(2.5)
        time.sleep(8)
        serv1.ChangeDutyCycle(12.5)
        serv2.ChangeDutyCycle(12.5)
        serv3.ChangeDutyCycle(12.5)

    time.sleep(5)
    serv1.stop()
    serv2.stop()
    serv3.stop()

def clean_exit():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        main()
        clean_exit()
    except:
        clean_exit()
        sys.exit(1)