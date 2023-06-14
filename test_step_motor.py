import RPi.GPIO as GPIO
import time
 
in1 = 17
in2 = 16
in3 = 13
in4 = 12
ENA = 5
ENB = 4
 
# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = .025
 
step_count = 1500
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( ENA, GPIO.OUT )
GPIO.setup( ENB, GPIO.OUT )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )
 
# initializing
GPIO.output( ENA, GPIO.HIGH )
GPIO.output( ENB, GPIO.HIGH )
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )
 
 
def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()
 
 
# the meat
def small_run():
    for i in range(1500):
        if i%4==0:
            print('')
            GPIO.output( in1, GPIO.HIGH )
            GPIO.output( in3, GPIO.LOW )
            GPIO.output( in2, GPIO.LOW )
            GPIO.output( in4, GPIO.LOW )
        elif i%4==1:
            print('2')
            GPIO.output( in1, GPIO.LOW )
            GPIO.output( in3, GPIO.LOW )
            GPIO.output( in2, GPIO.HIGH )
            GPIO.output( in1, GPIO.LOW )
        elif i%4==2:
            print('3')
            GPIO.output( in4, GPIO.LOW )
            GPIO.output( in3, GPIO.HIGH )
            GPIO.output( in2, GPIO.LOW )
            GPIO.output( in1, GPIO.LOW )
        elif i%4==3:
            print('4')
            GPIO.output( in1, GPIO.LOW )
            GPIO.output( in3, GPIO.LOW )
            GPIO.output( in2, GPIO.LOW )
            GPIO.output( in4, GPIO.HIGH )
        time.sleep( step_sleep )

small_run()
cleanup()
print('key 2 done')
exit( 0 )