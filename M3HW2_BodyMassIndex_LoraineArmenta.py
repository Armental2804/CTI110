# BMI
# 20170618
# CTI-110 M3HW2 - Body Mass Index
# Loraine Armenta
#
height = int( input ('Enter height using inches: '))
weight = int( input ('Enter weight using pounds: '))
bmi = (weight/ (height*height)) *703.0
print('This is your BMI', (bmi))

if bmi >= 0:
    print (' You are considered under weight')
else:
    if bmi >= 18.5:
        print ('You are at an optimal weight')
    else:
        if bmi >= 25:
            print('You are considered over weight')



            
