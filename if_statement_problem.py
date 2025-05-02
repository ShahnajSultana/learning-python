#Price of a house is $1M
#If buyer has good credit, they need to put down 10%
#Otherwise they need to put down 20
#Print the down payment

house_price = 1000000

has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price

print(f"Down payment ${down_payment}")