# accept two numbers and an operation, and then perform the operation on the two numbers
print("Simple calculator!")
first_number = input("First number? ")
opreator = input("Operation? ")
second_number = input("Second number? ")

opreator_list = ["+", "-", "*", "**", "%", "/"]

if first_number.isnumeric() == False or second_number.isnumeric() == False:
    print("Please input a number.")
    exit()
elif opreator not in opreator_list:
    print("Operation not recognized.")
    exit()
else:
    print("product of " + first_number + " " + opreator + " " + second_number + " equals", 
    eval(first_number + opreator + second_number))