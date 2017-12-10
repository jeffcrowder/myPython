import paho.mqtt.client as mqttClient
import RPi.GPIO as GPIO
import socket
import random
import datetime
import json
import time
import sys
import os

def getCPUtemp():
    res=os.popen('vcgencmd measure_temp').readline()
    cTemp = res.replace("temp=","").replace("'C\n","")
    fTemp =(9.0/5.0*(float(cTemp))) + 32
    return(round(fTemp,2))

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print "Connected to MQTTbroker " + configDict['broker']
        global Connected
        Connected = True
    else:
        print("Connection to MQTTbroker failed")

def readConfig():
    global configDict
    configDict = {}
    configDict = json.load(open("/home/pi/myPython/mqtt/config.json"))

def setupIO():
    global pin
    pin = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def flashLed():
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.03)
    GPIO.output(pin, GPIO.LOW)

def messageData():
    jsonData = {'hostname':'', 'time':'','temp':''}
    jsonData['hostname'] = socket.gethostname()
    #jsonData['time'] = time.ctime()
    jsonData['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    jsonData['temp'] = getCPUtemp()
    return json.dumps(jsonData)

def setupMQTT():
    broker_address= configDict['broker']
    port = int(configDict['port'])
    global client
    randNum = random.randint(0,1000)
    randName = socket.gethostname() + "_" + str(randNum)
    print "Mqtt Client Name = " + randName
    client = mqttClient.Client(randName)
    client.on_connect= on_connect
    client.connect(broker_address, port=port)

def destroy():
    print "\nExiting"
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    client.disconnect()
    client.loop_stop()

###################################
## Start the program here #########

Connected = False
readConfig()
setupMQTT()
setupIO()

client.loop_start()

while Connected != True:
    flashLed()

try:
    while True:
        client.publish(configDict["topic"], messageData())
        #sys.stdout.write("Message Sent: " + str(temperature) + "\r")
        #sys.stdout.flush()
        flashLed()
        time.sleep(configDict["updateSec"])

except KeyboardInterrupt:
    destroy()

