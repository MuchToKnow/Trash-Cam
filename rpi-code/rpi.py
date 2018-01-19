import requests
import base64
import numpy as np
import cv2
import json
import RPi.GPIO as GPIO
import time
import sys
import signal
import thread


img_path = "im2.jpg"
url = "http://35.163.191.108:3000/api/request"
OTIME = 5  # How long the bins are open for
CLOSE_DC = 10.5  # Duty Cycle for closed servo
OPEN_DC = 2.5  # Duty Cycle for open servo

aves = [10000, 10000, 10000, 10000] 
aveidx = 0
cooldown = 10
servLock = "9"

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

def open_bin(binNum, s1, s2, s3):
    global servLock
    # Compost
    if jsresp == 1:
        servLock = "1"
        serv1.ChangeDutyCycle(OPEN_DC)
        time.sleep(OTIME)
        serv1.ChangeDutyCycle(CLOSE_DC)
    # Recycle
    elif jsresp == 2:
        servLock = "2"
        serv2.ChangeDutyCycle(OPEN_DC)
        time.sleep(OTIME)
        serv2.ChangeDutyCycle(CLOSE_DC)
    # Trash
    elif jsresp == 3:
        servLock = "3"
        serv3.ChangeDutyCycle(OPEN_DC)
        time.sleep(OTIME)
        serv3.ChangeDutyCycle(CLOSE_DC)
    # ALL
    else:
        servLock = "1230"
        serv1.ChangeDutyCycle(OPEN_DC)
        serv2.ChangeDutyCycle(OPEN_DC)
        serv3.ChangeDutyCycle(OPEN_DC)
        time.sleep(OTIME)
        serv1.ChangeDutyCycle(CLOSE_DC)
        serv2.ChangeDutyCycle(CLOSE_DC)
        serv3.ChangeDutyCycle(CLOSE_DC)
    # time.sleep(2)
    servLock = "9"

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

    # Start the Servos
    serv1.start(CLOSE_DC)
    serv2.start(CLOSE_DC)
    serv3.start(CLOSE_DC)

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

        isObj = large_enough(img, 2000)

        if isObj and cooldown < 0:
            cooldown = 10
            b64img = base64.b64encode(jimg)

            print("Sending POST")
            r = requests.post(url, json={"image" : b64img})

            jsresp = r.json()["status"]
            print(jsresp)

            while not jsresp in servLock:
                pass

            thread.start_new_thread( open_bin, (jsresp, serv1, serv2, serv3))

        else:
            cooldown = cooldown - 1

    print("Stopping Servos")
    serv1.stop()
    serv2.stop()
    serv3.stop()
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
