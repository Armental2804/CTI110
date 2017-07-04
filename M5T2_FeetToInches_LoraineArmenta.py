# ft to in'
# 20170704
# CTI-110 M5T2_FeetToInches 
# Loraine Armenta
#
INCHES_PER_FOOT = 12

def main ():
    feet = int (input ( 'Enter a number of feet: ' ))

    print (feet, 'equals' , feet_to_inches (feet), 'inches.')

def feet_to_inches (feet):
    return feet * INCHES_PER_FOOT

main ()
