user_input = input("Would you like to continue? ")
if user_input == "no" or user_input == "n":
    print("Exiting")
elif user_input == "yes" or user_input == "y":
    print("Continuing ...\nComplete!")
else:
    print("Please try again and respond with yes or no.")