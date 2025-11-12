# BEGINNING OF CODE
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.IN) # For IR sensor
GPIO.setup(26,GPIO.OUT) # For LED

try: 
   while True:
      if (GPIO.input(16)):
          print("No object")
          GPIO.output(26,GPIO.LOW) # LED OFF when no object detected
      else:
          print("Object Detected")
          GPIO.output(26,GPIO.HIGH) # LED ON when object detected
except KeyboardInterrupt:
    GPIO.cleanup()
# END OF CODE
