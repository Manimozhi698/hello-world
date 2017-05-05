a = int(input("Enter the temp in number "))
try:
 fahrenheit = float(a)
 celsius = (fahrenheit - 32.0) *5.0/9.0
 print (celsius)
except:
 print ("You didn't enter the fahrenheit,Enter first!!!!")
