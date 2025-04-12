import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(8, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(10, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(12, GPIO.OUT, initial = GPIO.HIGH)





time.sleep(3)
GPIO.cleanup()

