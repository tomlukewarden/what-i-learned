# Range searches through the range given as a parameter

for i in range(10):
    print(i)

# The range that will be printed in the terrminal is 0-9, so if I wanted to print the number 10, i would have to put 11

''' Below is an example of this but with the use of input from the user'''

# get user input of a number
max_num = int(input('The range is '))

# print as a loop e.g. if they input 10, print all numbers from 0-9
for i in range(max_num):
    print(i)