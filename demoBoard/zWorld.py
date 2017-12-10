import RPi.GPIO as GPIO
import json
import time

switchOneState = 0
switchTwoState = 0
switchThreeState = 0
switchFourState = 0

def initialize():
    print "setup the GPIO"
    readConfig()

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(led1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(led2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(led3, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(led4, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(buzz, GPIO.OUT, initial=GPIO.HIGH)
    
    GPIO.setup(sw1, GPIO.IN)
    GPIO.setup(sw2, GPIO.IN)
    GPIO.setup(sw3, GPIO.IN)
    GPIO.setup(sw4, GPIO.IN)

def readConfig():
    print "read a JSON file to setup pins to be used on RPI"
    global led1, led2, led3, led4
    global sw1, sw2, sw3, sw4
    global buzz
    
    d = {}
    d = json.load(open("/home/pi/myPython/demoBoard/config.json"))
    led1 = d['led1']
    led2 = d['led2']
    led3 = d['led3']
    led4 = d['led4']
    sw1 = d['sw1']
    sw2 = d['sw2']
    sw3 = d['sw3']
    sw4 = d['sw4']
    buzz = d['buzz']

def sw1State():
    return switchOneState

def sw2State():
    return switchTwoState

def sw3State():
    return switchThreeState

def sw4State():
    return switchFourState


def myCallback1(sw1):
    #print "callback sw1"
    global switchOneState
    if switchOneState == 1:
        switchOneState = 0
    else:
        switchOneState = 1

def myCallback2(sw2):
    #print "callback sw2"
    global switchTwoState
    if switchTwoState == 1:
        switchTwoState = 0
    else:
        switchTwoState = 1

def myCallback3(sw3):
    #print "callback sw3"
    global switchThreeState
    if switchThreeState == 1:
        switchThreeState = 0
    else:
        switchThreeState = 1


def myCallback4(sw4):
    #print "callback sw4"
    global switchFourState
    if switchFourState == 1:
        switchFourState = 0
    else:
        switchFourState = 1

def setLed1(state):
    if state == 0:
        GPIO.output(led1,GPIO.HIGH)
    elif state == 1:    
        GPIO.output(led1,GPIO.LOW)
    else:
        print "wrong state = " + state

def setLed2(state):
    if state == 0:
        GPIO.output(led2,GPIO.HIGH)
    elif state == 1:    
        GPIO.output(led2,GPIO.LOW)
    else:
        print "wrong state = " + state

def setLed3(state):
    if state == 0:
        GPIO.output(led3,GPIO.HIGH)
    elif state == 1:    
        GPIO.output(led3,GPIO.LOW)
    else:
        print "wrong state = " + state

def setLed4(state):
    if state == 0:
        GPIO.output(led4,GPIO.HIGH)
    elif state == 1:    
        GPIO.output(led4,GPIO.LOW)
    else:
        print "wrong state = " + state

def setAllLed(state):
    if state == 0:
        GPIO.output(led1,GPIO.HIGH)
        GPIO.output(led2,GPIO.HIGH)
        GPIO.output(led3,GPIO.HIGH)
        GPIO.output(led4,GPIO.HIGH)
    elif state == 1:    
        GPIO.output(led1,GPIO.LOW)
        GPIO.output(led2,GPIO.LOW)
        GPIO.output(led3,GPIO.LOW)
        GPIO.output(led4,GPIO.LOW)
    else:
        print "wrong state = " + state

def setBuzzer(state):
    #print "set the buzzer and annoy everyone"
    if state == 0:
        GPIO.output(buzz,GPIO.HIGH)
    else:
        GPIO.output(buzz,GPIO.LOW)

def destroy():
    print "clear out the GPIO"
    GPIO.remove_event_detect(sw1)
    GPIO.remove_event_detect(sw2)
    GPIO.remove_event_detect(sw3)
    GPIO.remove_event_detect(sw4)
    GPIO.cleanup()

if __name__ == "__main__":
    print "program is being run standalone"
    initialize()
    GPIO.add_event_detect(sw1, GPIO.RISING, callback=myCallback1, bouncetime=200)
    GPIO.add_event_detect(sw2, GPIO.RISING, callback=myCallback2, bouncetime=200)
    GPIO.add_event_detect(sw3, GPIO.RISING, callback=myCallback3, bouncetime=200)
    GPIO.add_event_detect(sw4, GPIO.RISING, callback=myCallback4, bouncetime=200)
    
    try:
        while True:
            setLed1(1)
            setLed2(1)
            setLed3(1)
            setLed4(1)
            #setBuzzer(1)
            time.sleep(5)
            #setBuzzer(0)
            setLed1(0)
            setLed2(0)
            setLed3(0)
            setLed4(0)
            time.sleep(5)
    except KeyboardInterrupt:
        destroy()
else:
    try:

        print "program is being imported as a module"
        initialize()
        GPIO.add_event_detect(sw1, GPIO.BOTH, callback=myCallback1, bouncetime=200)
        GPIO.add_event_detect(sw2, GPIO.BOTH, callback=myCallback2, bouncetime=200)
        GPIO.add_event_detect(sw3, GPIO.BOTH, callback=myCallback3, bouncetime=200)
        GPIO.add_event_detect(sw4, GPIO.BOTH, callback=myCallback4, bouncetime=200)
    except KeyboardInnterrupt:
        destroy()

