#This prevents an error if someone enters 0 as the divisor

dividen, divisor = eval(input('Please enter numbers to divide: '))
#If posible report the result if possible
if divisor != 0:
    print(dividen, '/', divisor, "=", dividen/divisor)
else:
    print('Fuck u')
