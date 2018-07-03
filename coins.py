coins = 0
user_input = raw_input('Would you like a coin? (Y/N) ')

if user_input.lower() == 'y' or 'yes':
    coins += 1
    print "You now have %d coins." % coins
else:
    print "Have a nice day."