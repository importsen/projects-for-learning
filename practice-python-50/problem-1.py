'''
create a program to ask the user to enter their name and age. print out a 
a message addressed to them that tells them the year that they will turn 100
years old.
'''
#question driven development
# how do i take in the user input for the name and age?
# how do i calculate the year they will turn 100 from the input?

name = input("what is your name? ")
age = input("what is your age? ")

oldAge = 100 - int(age)
oldAgeYear = 2023 + oldAge

print("You will turn 100 in " + str(oldAgeYear))

askNumber = int(input("pick a number "))

repeatQuestion = askNumber * "pick a number\n"

print(repeatQuestion)

#extras:
# 1. ask the user for another number, and printing that many copies of the 
# previous question 
# 2. print out that many copies of the previous message on seperate lines
