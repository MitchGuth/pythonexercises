day = int(raw_input('Day 0-6? '))
day_of_the_week = day
if day_of_the_week == 0:
    print 'Sunday'
elif day_of_the_week == 1:
    print 'Monday'
elif day_of_the_week == 2:
    print 'Tuesday'
elif day_of_the_week == 3:
    print 'Wednesday'
elif day_of_the_week == 4:
    print 'Thursday'
elif day_of_the_week == 5:
    print 'Friday'
elif day_of_the_week == 6:
    print 'Saturday'
else:
    print 'That is not a number between 0-6'

print ''

day = int(raw_input('Day 0-6? '))
day_of_the_week = day
if day_of_the_week == 0 or day_of_the_week == 6:
    print 'Sleep in you deserve it!'
elif day_of_the_week > 0 and day_of_the_week < 6:
    print 'You better go to work today!'
else:
    print 'That is not a number between 0-6'

print ''

print 'Would you like to convert temperature from Celsius to Farenheit?'
temperature_c = raw_input('What is the temperature in Celsius? ')
temperature_c = int(temperature_c)
temperature_f = temperature_c * 1.8 + 32
print 'It is then ' + str(temperature_f) + ' degrees Farenheit'

print ''
print ''

print 'Here is some help to calculate your tip.'
bill_input = raw_input('How much was your bill?')
bill = float(bill_input)
tip = 0
bill_total = 0
level_of_service = raw_input('How would you rate your service? good, fair or bad? ')
level_of_service = level_of_service.lower()

if level_of_service == 'good':
    tip = bill * 0.20
    bill_total = tip + bill
    print 'You should tip $%.2f for the service.'% tip
    print 'Your total bill is $%.2f'% bill_total
elif level_of_service == 'fair':
    tip = bill * 0.15
    bill_total = tip + bill
    print 'You should tip $%.2f for the service.' % tip
    print 'Your total bill is $%.2f'% bill_total
elif level_of_service == 'bad':
    tip = bill * 0.10
    bill_total = tip + bill
    print 'You should tip $%.2f for the service.' % tip
    print 'Your total bill is $%.2f' % bill_total
else:
    print 'You may have entered in something incorrectly.'

print ''
print ''

print 'Here is some help to calculate your tip, I will even split the check evenly.'
bill_input = raw_input('How much was your bill?')
bill = float(bill_input)
tip = 0
bill_total = 0
level_of_service = raw_input('How would you rate your service? good, fair or bad? ')
level_of_service = level_of_service.lower()
split_number = raw_input('How many ways should the bill be split? ')
split_number = int(split_number)

if level_of_service == 'good':
    tip = bill * 0.20
    bill_total = tip + bill
    print 'You should tip $%.2f for the service.'% tip
    print 'Your total bill is $%.2f'% bill_total
elif level_of_service == 'fair':
    tip = bill * 0.15
    bill_total = tip + bill
    print 'You should tip $%.2f for the service.' % tip
    print 'Your total bill is $%.2f'% bill_total
elif level_of_service == 'bad':
    tip = bill * 0.10
    bill_total = tip + bill
    print 'You should tip $%.2f for the service.' % tip
    print 'Your total bill is $%.2f' % bill_total
else:
    print 'You may have entered in something incorrectly.'

split_cost = float(bill_total) / split_number
print 'Cost per person $%.2f' % split_cost