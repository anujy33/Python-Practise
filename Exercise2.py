# Script that can be used to convert Temp from Celsius to Fahrenheit or vice versa

#!/usr/bin/python

v1 = raw_input("Enter the Temp in celsius:")
try:
	f = eval(v1) * (9.0)/5 + 32
	print "Temp in Fahrenheit:" , f
except:
	print "Enter the value in digits"
	
v2 = raw_input("Entet the temp in Fahrenheit: ")
try:
	c = (eval(v2) - 32) * 5.0/9
	print "Temp in Celsius: ", c
except:
	print " Enter the value in digits it seems you have given string"
	