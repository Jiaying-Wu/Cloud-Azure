# type() function
print(type('7'))
print(type(7))
print(type(7.1))

# isinstance() function
print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))

# create a Boolean expression by using the type() function
print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)

# relationship between data types and variables
x = 'a string'
print(type(x))
x = 7
print(type(x))
x = False 
print(type(x))