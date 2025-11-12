# BEGINNING OF CODE
# SINGLE LED ON/OFF
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
try:
  while True:
      print(“LED ON”)
      GPIO.output(16,GPIO.HIGH)
      time.sleep(1)
      print(“LED OFF”)
      GPIO.output(16,GPIO.LOW)
      time.sleep(1)
except:
  GPIO.cleanup()

##########

# TWO LEDs ON/OFF
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
try:
  while True:
      print(“LED ON”)
      GPIO.output(16,GPIO.HIGH)
      GPIO.output(26,GPIO.HIGH)
      time.sleep(1)
      print(“LED OFF”)
      GPIO.output(16,GPIO.LOW)
      GPIO.output(26,GPIO.LOW)
      time.sleep(1)
except:
  GPIO.cleanup()

##########

# BUZZER WITH ONE LED ON/OFF
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
try:
  while True:
    print("LED Buzzer ON")
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)
    time.sleep(1)
    print("LED & Buzzer OFF")
    GPIO.output(16,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    time.sleep(1)
except:
  GPIO.cleanup()

##########
# END OF CODE
