name = raw_input('What is your name? ')
print 'Hello, ' + name + '!'
print ''

name = raw_input('What is your name? ')
message = 'Hello, ' + name.upper() + '!'
number = len(name)
print message.upper()
totalMessage = 'Your name has ' + str(number) + ' letters in it! Awesome!'
print totalMessage.upper()

print ''

print 'Welcome to the madlib game!'
noun = raw_input('Please enter a person\'s name: ')
adjective = raw_input('Please enter an adjective: ')
action = raw_input('Please enter a verb: ')

print noun + ' is ' + adjective + ' and is also great at ' + action + '!'

print ''

keepGoing = raw_input('Would you like to keep playing (Y/N)?')
if keepGoing == 'Y' or keepGoing == 'y' or keepGoing == 'yes' or keepGoing == 'Yes' or keepGoing == 'YES':
    print 'Here we go again...'
    noun2 = raw_input('Please enter a person\'s name: ')
    adjective2 = raw_input('Please enter an adjective: ')
    action2 = raw_input('Please enter a verb: ')

    print noun2 + ' is ' + adjective2 + ' and is also great at ' + action2 + '!'

else:
    print 'Have a great rest of your day.'