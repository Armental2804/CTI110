# Bug Collector Project
# 20170625
# CTI-110 M4T1 - Bug Collector
# Loraine Armenta
#
# Total amount of days 5
days = 5
# Total number of bugs collected in five days
number_of_bugs = 0
# How many bugs were collected
for todate in range(1, days + 1):
    bugs_collected = int (input ('How many bugs were collected on day'\
                                 + str (todate ) + ':' ))
    number_of_bugs = number_of_bugs + bugs_collected
print()
print( ' The total number of bugs collected in all', days, 'days is', \
       number_of_bugs )
