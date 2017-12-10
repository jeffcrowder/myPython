import zWorld as zw
import time
import sys

sys.dont_write_bytecode = True

# functions to read switches: sw1State(), sw2State(),sw3State(), sw4State()
# functions to set Leds: setLed1(val), setLed2(val), setLed3(val), setLed4(val), setAllLed(val)
# function to set Buzzer: setBuzzer(val)

try:
    while True:
        
        if zw.sw1State() == 1:
            zw.setLed1(1)
        else:
            zw.setLed1(0)
        
        sys.stdout.write(str(zw.sw1State()) + " | " + str(zw.sw2State()) + " | " + str(zw.sw3State()) + " | " + str(zw.sw4State()) + "\r")

        time.sleep(.001)

except KeyboardInterrupt:
    zw.destroy()



