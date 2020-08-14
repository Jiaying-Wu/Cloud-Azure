# convert temperatures from Fahrenheit to Celsius
fahrenheit = input("What is the temperature in fahrenheit? ")
if fahrenheit.isnumeric():
    print("Temperature in celsius is", int((int(fahrenheit) - 32) * 5/9))
else:
    print("Input is not a number.")