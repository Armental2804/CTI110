# Age Class
# 20170618
# CTI-110 M3HW1 - Age Classifier
# Loraine Armenta
#If the person is 1 year old or less, he or she is an infant
#If the person is older than 1 years, but younger than 13 years he or she is a child
#If the person is at least 13 years old, but less than 20 years old, they are teens
#if the person is at least 20 years old, they are an adult


# Age ranges
infant = 1
child = 2
teenager = 13
adult = 20

# Enter Age
age = int(input(' Enter your age: '))

if age >= adult:
    print(' Your an adult.')
else:
    if age >= teenager:
        print(' Your a teenager ')
    else:
        if age >= child:
            print(' Your a child ')
        else:
            print(' Your a infant ')
            
