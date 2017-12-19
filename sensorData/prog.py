from CpuTemp import CpuTemp 

tempF = CpuTemp(False)
print(tempF.getValue())

tempC = CpuTemp(True)
print(tempC.getValue())

