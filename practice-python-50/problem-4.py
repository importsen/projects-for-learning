"""
create a program that asks the user for a number and then prints out a list of
all the divisors of that number. 
"""

#num = int(input("pick a number: "))

#x = (range(0, 100))

#valid_nums = []

#for i in x:
#    if num % x == 0:
#        valid_nums.append()
#        print(valid_nums)

num = int(input("pick a number to divide: "))

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
