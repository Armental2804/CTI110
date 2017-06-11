# Tip Tax and Total Project
# 20170610
# CTI-110 M2HW2-Tip Tax Total
# Loraine Armenta
#

#Get the charge for food.
total = float (input ('Enter the total amount of meal purchased:'))

# Calculate the 18 percent tip and 7 percent sales tax
tip = 0.18*total

sales_tax = 0.07*total

total_amount = total + tip + sales_tax

 
# Display the each amount and total
print ('18 percent tip $%s' % format(tip,'.2f'))

print ('7 percent sales tax $%s' % format (sales_tax, '.2f'))

print ('Total amount = $%s' % format (total_amount, '.2f'))

