# accept an input parameter
# leave out the argument
# second optional input parameter
def say_hello(name='World', greeting=None):
  if greeting == None:
    print(f'Hello {name}!')
  else:
    print(f'{greeting} {name}!')

say_hello()
say_hello('Bob')
say_hello(greeting='Howdy')
say_hello('Bob', 'Howdy')

# NoneType object
print(type(None))

say_hello(greeting='Howdy')
say_hello('Bob', 'Howdy')

# add a new function that returns a value
def add_two_numbers(x, y):
    return x + y

add_two_numbers(4, 6)
result = add_two_numbers(5, 7)
print(result)

# add a new function that returns a list
def create_deck():
  suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck = []

  for  suit in suits:
    for rank in ranks:
      deck.append(f'{rank} of {suit}')

  return deck

my_deck = create_deck()
print(len(my_deck))

# demonstrates variable scope in a function
value = 1

def some_function():
    value = 10
    return value

print(value)
some_function()
print(value)