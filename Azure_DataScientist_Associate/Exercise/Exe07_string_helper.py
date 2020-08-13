# capitalize() function
message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())

# modify the case of the string
message = 'hello world'
print(message.lower())
print(message.upper())

message = message.title()
print(message)
print(message.swapcase())

# counts the number of specific letter in a string
location = 'Mississippi'
print(location.count('s'))

# count number of letters in a string
print(len('how many letters in this string?'))

# check the letters of a string start with or end with
message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

# find position of a string inside another string
message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))

# strips empty characters from the left or right, or both
message = '    middle     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')

# replace pattern in string
message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)

# justifies a string by adding empty space characters
message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))