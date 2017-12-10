import sys
import time
import RPi.GPIO as GPIO
import socket
import datetime
import json

GPIO.setmode(GPIO.BCM)

mode = GPIO.getmode()
print mode

GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.HIGH)
time.sleep(1)
GPIO.output(12,GPIO.LOW)
time.sleep(1)
GPIO.output(12,GPIO.HIGH)
time.sleep(1)
GPIO.output(12,GPIO.LOW)
GPIO.cleanup()

d = {'hostname':'','time':'','temp':''}
print(d)
d['hostname'] = "blah_" + socket.gethostname()
d['time'] = time.ctime()
d['temp'] = 105
print(d)

print("\nKEYS ") 
print(d.keys())
print("\nVALUES ")
print(d.values())
print("\nITEMS " )
print( d.items())

jdata = json.dumps(d)

print "\njson"
print(jdata)

j={}
j = json.loads(jdata)
print "\njson to dict"
print(j)

print(j['hostname'])
print(j['time'])
print(j['temp'])

d.clear()
print(d)

print "Hello World!"
print "Hello Again"

print("#############")
blah = open("config.pub.json")
jblah = json.load(blah)
print(jblah)
print("#############")


sys.stdout.write('adsfasd: ')
sys.stdout.write ('\r')
sys.stdout.flush()
time.sleep(1)
sys.stdout.write('qewrqwety\n')
sys.stdout.flush()

time.sleep(1)
