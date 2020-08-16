# a function accepting an arbitrary arguments list
def print_args(*args):
  for arg in args:
    print(f'arg = {arg}')

print_args('a')
print_args('a', 'b')
print_args('a', 'b', 'c')

# add code that accepts keyword arguments
# iterate through each keyword and value
# print the value of kwargs and its data type
def print_keyword_args(**kwargs):

  print('\n')
  print(kwargs)
  print(type(kwargs))

  for key, value in kwargs.items():
    print(f'{key} = {value}')

  third = kwargs.get('third', None)
  if third != None:
    print('third arg =', third)


print_keyword_args(first='a')
print_keyword_args(first='b', second='c')
print_keyword_args(first='d', second='e', third='f')