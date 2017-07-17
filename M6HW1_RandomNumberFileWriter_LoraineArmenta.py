# Random number
# Date
# CTI-110 M6HW1 - Random Number File Writer
# Loraine Armenta
#
import random

file = open('Random.txt','w')

for i in range(int(input('The random numbers range up to 500!:'))):
    line = str(random.randint(1, 500))
    file.write(line)
    print(line)

file.close()
