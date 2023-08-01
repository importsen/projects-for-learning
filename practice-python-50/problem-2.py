'''
1. ask the user for a number. depending on whether the number is even or odd,
print out the appropriate message to the user.

2. ask the user for a number. depending on whether the number is even or odd, 
print out an appropriate message

extras: 

if the number is a multiple of 4m print out a different message

ask the user for two numbers: one number to check (num) and one number to 
divide (check). if check divides evenly into num, tell that to the user if 
not, print a different appropriate message to the user
'''

userInput = input("type a number: ") 

if userInput.isdigit(): # check if the input is only digits
    number = int(userInput) #convert the input to integer
    if number % 2 == 0: 
        print("Your message is a even number!") 
    if number % 4 == 0:
        print("this number is a multiple of 4!")
    elif number % 2 != 0:
        print("your message is a odd number!")
else:
    print("please enter a valid number!") 
