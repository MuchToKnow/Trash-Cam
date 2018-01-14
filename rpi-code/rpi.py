import requests
import base64
from cv2 import *
import json
import RPi.GPIO as GPIO
import time


img_path = "im2.jpg"
url = "http://35.163.191.108:3000/api/request"

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
#serv1 = GPIO.PWM(11, 50)
#GPIO.setup(13, GPIO.OUT)
#serv2 = GPIO.PWM(13, 50)
#GPIO.setup(15, GPIO.OUT)
#serv3 = GPIO.PWM(15, 50)

print("Starting img capture")
cam = VideoCapture(0)
s, img = cam.read()

s, jimg = imencode(".jpeg", img)

b64img = base64.b64encode(jimg)

print("Sending POST")
r = requests.post(url, json={"image" : b64img})

jsresp = r.json()["status"]
print(jsresp)

#serv1.start(2.5)
#serv2.start(2.5)
#serv3.start(2.5)

time.sleep(5)

#serv1.stop()
#serv2.stop()
#serv3.stop()

#GPIO.cleanup()
