"""
take a list and write a program that prints out all the elements of the list 
that are less then 5.

extras: 

1. instead of printing the elements one by one, make a new list that 
has all the elements less then 5 from this list in it and print out this new 
list

2. write this in one line of python

3. ask the user for a number and return a list that contains only elements 
from the original list 'a' that are smaller then that number given by the 
user.
"""

#full_list = [1, 1, 2, 3, 5, 8, 12, 21, 34, 55, 89]

#part_list = 
#part_list.append(0)
#for i in part_list:
#    print(part_list)
    


#new_a = for i in a:
#    if i > 5:
#   print(a)

# i cant figure it out
#solution:

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

lessFNumbs = []
moreFNumbs = []

for num in numbers:
    if num < 5:
        lessFNumbs.append(num)
        lessFNumbs.sort()
print(lessFNumbs)

#basic problem
for i in numbers:
    if i < 5:
        print(i)


