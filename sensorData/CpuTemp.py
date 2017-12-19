import os

class CpuTemp():
    """Class to read the rpi CPU temperature"""

    metric = True

    def __init__(self, metric):
        if metric:
            print("Celsius")
            self.metric = metric 
        else:
            print("Farenheit")
            self.metric = metric 

    def getValue(self):
        """Return a string containing cpu temp"""
        temperature = self.getCPUtemp() 

        if self.metric:
            return temperature 
        else:
            temperature = self.convCtoF(temperature)
        return temperature 

    def getCPUtemp(self):
        res=os.popen('vcgencmd measure_temp').readline()
        temp = res.replace("temp=","").replace("'C\n","")
        return temp

    def convCtoF(self,tempC):
        tempF = (9.0/5.0*(float(tempC))) + 32
        return tempF

