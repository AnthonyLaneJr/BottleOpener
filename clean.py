import RPi.GPIO as GPIO

in1 = 17
in2 = 16
in3 = 13
in4 = 12
 
# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = .5
 
step_count = 400
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )
GPIO.cleanup()