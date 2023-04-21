import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # logic numeration

# working with pins LED-STATUS 
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # GREEN
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # RED

# working with pins LED-01 
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) # GREEN
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) # RED

# working with pins LED-02 
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) # GREEN
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW) # RED

# working with pins LED-03 
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) # GREEN
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW) # RED



# pin on GREEN
GPIO.output(26, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)

input()

# pin off
GPIO.output(26, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
sleep(1)
GPIO.output(21, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)

input()

# on exit
GPIO.output(21, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.cleanup()


