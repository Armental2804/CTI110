# Sum of Numbers Project
# 20170625
# CTI-110 M4HW1 - Sum of Numbers
# Loraine Armenta
#

total_number = 0

the_number = float( input(' Enter users first number or negative '+ \
                        'number to end the series:') )

while the_number > -1:
    total_number = total_number + the_number
    the_number = float( input(' Enter users following number or the '+ \
                            'negative number to end the series  :') )
print ('')
print (' The total of all the numbers entered is', total_number )
