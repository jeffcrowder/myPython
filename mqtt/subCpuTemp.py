import paho.mqtt.client as mqttClient
import sqlite3
import socket
import random
import json
import time
import sys

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

def on_message(client, userdata, message):
    theDict = json.loads(message.payload)
    #print(theDict)
    db = sqlite3.connect("/home/pi/myPython/mqtt/CPUtemp.db")
    cursor = db.cursor()
    cursor.execute('''INSERT INTO temperature(timeStamp, hostname, tempData)VALUES(?,?,?)''', (theDict['time'],theDict['hostname'],theDict['temp']))
    db.commit()
    db.close()

def setupMQTT():
    broker_address= configDict['broker']
    port = int(configDict['port'])
    global client
    randNum = random.randint(0,1000)
    randName = socket.gethostname() + "_" +  str(randNum)
    print "MQTT Client Name = " + randName
    client = mqttClient.Client(randName)
    client.on_connect= on_connect
    client.connect(broker_address, port=port)

def destroy():
    print "\nExiting"
    client.disconnect()
    client.loop_stop()

###################################
## Start teh program here ########

Connected = False
readConfig()
setupMQTT()

client.on_message= on_message
client.loop_start()

while Connected != True:
    time.sleep(0.1)

client.subscribe(configDict["topic"])
#client.subscribe("piTemp")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    destroy()
