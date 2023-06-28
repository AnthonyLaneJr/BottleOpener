import RPi.GPIO as GPIO
import time
 
Hin1 = 17
Hin2 = 16
Vin1 = 13
Vin2 = 12 
ENA = 5  #3 ribbons for ENA
ENB = 4  #3 ribbons for ENB
trigger = 19   # sends signal
echo = 20   # reads return

step_sleep = (.005)
 
step_count = 2000
 
# setting up
GPIO.setmode(GPIO.BCM)
GPIO.setup( ENA, GPIO.OUT )
GPIO.setup( ENB, GPIO.OUT )
GPIO.setup( Hin1, GPIO.OUT )
GPIO.setup( Hin2, GPIO.OUT )
GPIO.setup( Vin1, GPIO.OUT )
GPIO.setup( Vin2, GPIO.OUT ) 
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
 
# initializing
GPIO.output( ENA, GPIO.HIGH )
GPIO.output( ENB, GPIO.HIGH )
GPIO.output( Hin1, GPIO.LOW )
GPIO.output( Hin2, GPIO.LOW )
GPIO.output( Vin1, GPIO.LOW )
GPIO.output( Vin2, GPIO.LOW )
 
 
def cleanup():
    GPIO.output( Hin1, GPIO.LOW )
    GPIO.output( Hin2, GPIO.LOW )
    GPIO.output( Vin1, GPIO.LOW )
    GPIO.output( Vin2, GPIO.LOW )
    GPIO.cleanup()
 
def distance():
    GPIO.output(trigger, GPIO.HIGH)
    
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)
    
    Start = time.time()
    Stop = time.time()
    
    while GPIO.input(echo) == 0:
        Start = time.time()
        
    while GPIO.input(echo) == 1:
        Stop = time.time()
        
    TimeElapsed = Stop - Start
    
    distance = (TimeElapsed * 34300) / 2
    
    return distance

def small_run(step_count):
    for i in range(step_count):
        GPIO.output( Hin1, GPIO.HIGH )
        print(i)
    GPIO.output( Hin1, GPIO.LOW )
    
        
        
small_run(step_count)
cleanup()