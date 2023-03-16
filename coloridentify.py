import RPi.GPIO as GPIO
import time



pin2 = 23
pin3 = 24
signal = 25
cycles= 10


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(pin2,GPIO.OUT)
  GPIO.setup(pin3,GPIO.OUT)
  print("\n")
  




def loop():
  tempvar = 1
  while(1):  

    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(cycles):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start 
    red  = cycles / duration   
   
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(cycles):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = cycles / duration
    

    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(cycles):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = cycles / duration
    
      
    if green<7000 and blue<7000 and red>12000:
      print("red")
      tempvar=1
    elif red<12000 and  blue<12000 and green>12000:
      print("green")
      tempvar=1
    elif green<7000 and red<7000 and blue>12000:
      print("blue")
      tempvar=1
    elif red>10000 and green>10000 and blue>10000 and tempvar==1:
      print("No object detected! please place the object.")
      tempvar=0


def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
