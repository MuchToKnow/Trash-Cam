import requests
import base64
import numpy as np
import cv2
import json
import RPi.GPIO as GPIO
import time
import sys
import signal


img_path = "im2.jpg"
url = "http://35.163.191.108:3000/api/request"
aves = [10000, 10000, 10000, 10000] 
aveidx = 0
cooldown = 10

cont = True

def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
 
    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key = cv2.contourArea)
 
    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)[1]
 
def large_enough(image, threshold):
    global aveidx

    area = find_marker(image) 
    area = area[0] * area[1]
    print(area)

    aves[aveidx % len(aves)] = area
    area = sum(aves)/len(aves)
    aveidx = aveidx + 1

    print(area)
    return area < threshold

def main():
    global cooldown
    print("Initing GPIO and Webcam")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)
    serv1 = GPIO.PWM(13, 50)
    GPIO.setup(11, GPIO.OUT)
    serv2 = GPIO.PWM(11, 50)
    GPIO.setup(15, GPIO.OUT)
    serv3 = GPIO.PWM(15, 50)

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Unable to open camera")
        clean_exit()

    # Reset Servo Location
    serv1.start(10.5)
    serv2.start(10.5)
    serv3.start(10.5)
    time.sleep(1)
    serv1.stop()
    serv2.stop()
    serv3.stop()

    print(cont)
    while cont:
        print("Starting img capture")
        if cam.isOpened():
            s, img = cam.read()
        else:
            print("Camera Lost")
            clean_exit()
            sys.exit(1)

        s, jimg = cv2.imencode(".jpeg", img)

        isObj = large_enough(img, 6000)

        if isObj and cooldown < 0:
            cooldown = 10
            b64img = base64.b64encode(jimg)

            print("Sending POST")
            r = requests.post(url, json={"image" : b64img})

            jsresp = r.json()["status"]
            print(jsresp)

            # Compost
            if jsresp == 1:
                serv1.start(10.5)
                serv1.ChangeDutyCycle(2.5)
                time.sleep(8)
                serv1.ChangeDutyCycle(10.5)
                serv1.stop()
            # Recycle
            elif jsresp == 2:
                serv2.start(10.5)
                serv2.ChangeDutyCycle(2.5)
                time.sleep(8)
                serv2.ChangeDutyCycle(10.5)
                serv2.stop()
            # Trash
            elif jsresp == 3:
                serv3.start(10.5)
                serv3.ChangeDutyCycle(2.5)
                time.sleep(8)
                serv3.ChangeDutyCycle(10.5)
                serv3.stop()
            # ALL
            else:
                serv1.start(10.5)
                serv2.start(10.5)
                serv3.start(10.5)
                serv1.ChangeDutyCycle(2.5)
                serv2.ChangeDutyCycle(2.5)
                serv3.ChangeDutyCycle(2.5)
                time.sleep(8)
                serv1.ChangeDutyCycle(10.5)
                serv2.ChangeDutyCycle(10.5)
                serv3.ChangeDutyCycle(10.5)
                serv1.stop()
                serv2.stop()
                serv3.stop()

            time.sleep(5)
        else:
            cooldown = cooldown - 1

    print("Stopping Servos")
    cam.release()

def clean_exit():
    print("Cleaning up")
    GPIO.cleanup()

def signal_handler(signal, frame):
#        cont = False
        clean_exit()
        sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()

    """try:
        main()
        clean_exit()
    except Exception as e:
	print(e)
        clean_exit()
        sys.exit(1)
    """
