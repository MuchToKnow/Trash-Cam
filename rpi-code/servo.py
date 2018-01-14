import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)

p.start(2.5)
p.ChangeDutyCycle(12.5)		# turn toward 180 degree
time.sleep(5) 				# sleep 10 seconds
p.ChangeDutyCycle(2.5) 		# turn toward 0 degree
time.sleep(5)

p.stop()

GPIO.cleanup()
