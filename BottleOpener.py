import RPi.GPIO as GPIO
import time
 
in1 = 17
in2 = 16
in3 = 13
in4 = 12
ENA = 5  #2 ribbons for ENA
ENB = 4  #2 ribbons for ENB
trigger = 19   # sends signal
echo = 20   # reads return
 
# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = (.025)
 
step_count = 1500
 
# setting up
GPIO.setmode(GPIO.BCM)
GPIO.setup( ENA, GPIO.OUT )
GPIO.setup( ENB, GPIO.OUT )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
 
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

# the meat
def horizontal_run():
    GPIO.setmode(GPIO.BCM)
    for i in range(600):
        if i%4==0:
            print('1')
            GPIO.output( in1, GPIO.HIGH )
            GPIO.output( in3, GPIO.LOW )
            GPIO.output( in2, GPIO.LOW )
            GPIO.output( in4, GPIO.LOW )
        elif i%4==1:
            print('2')
            GPIO.output( in4, GPIO.LOW )
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
 
if __name__ == '__main__':
    while True:
        dist = distance()
        if dist < 5.5: 
            print (f'Bingo : {dist}')
            horizontal_run()
            print('done')
            time.sleep(2) 
        else:
            print(f'to far: {dist}')
        time.sleep(.01) 


cleanup()
print('key 2 done')
exit( 0 )