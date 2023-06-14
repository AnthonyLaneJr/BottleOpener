import RPi.GPIO as GPIO
import time

trigger = 19   # sends signal
echo = 20   # reads return


GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
    GPIO.output(trigger, True)
    
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    
    Start = time.time()
    Stop = time.time()
    
    while GPIO.input(echo) == 0:
        Start = time.time()
        
    while GPIO.input(echo) == 1:
        Stop = time.time()
        
    TimeElapsed = Stop - Start
    
    distance = (TimeElapsed * 34300) / 2
    
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            if dist < 5.5: 
                print (f'Bingo : {dist}')
                time.sleep(2) 
            else:
                print(f'to far: {dist}')
            time.sleep(.01) 
    except KeyboardInterrupt:
        print('measurement stopped by user')
        GPIO.cleanup()
        
        
        
        