import RPi.GPIO as GPIO
import time

#GPIO Pin labelling
Hin1 = 17
Hin2 = 16
Vin1 = 13
Vin2 = 12 
ENA = 5
ENB = 4  

trigger = 19   # sends signal
echo = 20   # reads return
 
# careful lowering this, at some point you run into the mechanical
# limitation of your motor
step_sleep = (.005)
 
step_count = 3000
 
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

#Control the  horizontal motor motion
def small_run(step_count):
    for i in range(step_count):
        GPIO.output( Hin1, GPIO.HIGH )
        time.sleep( step_sleep )
        GPIO.output( Hin1, GPIO.LOW )

#Function to control vertical motor motion,
#Takes in True of False boolean to control direction
def large_run(num = 1, reverse = False):
    num = int(num)+1
    if reverse == True:
            #print('V 1')
            GPIO.output( Vin2, GPIO.HIGH )
            time.sleep( step_sleep )
            GPIO.output( Vin2, GPIO.LOW )
    elif reverse == False:
        for i in range (0,num):
            #print('V 4')
            GPIO.output( Vin1, GPIO.HIGH )
            time.sleep( 1 )
        GPIO.output( Vin1 , GPIO.LOW )
    
            
#Lowers the system until the appropriate
#height is recorded, then activates opening  motor
#Finally returns to original height
def main_function():
        dist = distance()
        start = time.time()
        while dist > 5:
            large_run()
            dist = distance() 
        stop = time.time()
        verticle_return = stop-start
        print (f'Bingo : {dist}')
        small_run(step_count)
        large_run(verticle_return, reverse = True)
        print('done')
        time.sleep(2)  


main_function()

cleanup()
print('key 2 done')
exit( 0 )