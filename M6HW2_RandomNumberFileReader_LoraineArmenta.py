# File Reader
# 20170716
# CTI-110 M6HW2 - Random Number File Reader
# Loraine Armenta
#
import random

file = open('Random.txt', 'w')

random_numbers = int(input('The amount of numbers displayed from the file?:'))
print('The random numbers are:')

for i in range (random_numbers):
    number = random.randint(1,500)
    print(number)

file.write(str(number)+ '\n')
file.close()

file = open('Random.txt', 'r')
number = 0
total = 0
print('Listed of number:')
for line in file.readlines():
        print(line)
        total = total+int(line)
        number +=1
print('The total of the numbers! = '+str(total))
print('The number of random numbers read from the file! '+str(number))
print= int(int(input('The end!')))  
