num = range(1, 11)
print num

print ''

num = range(1, 11, 2)
print num

print ''

num = range(1, 11)
n = raw_input('What number from 1 to 10 would you like to start from? ')
m = raw_input('What number would you like to end on after your starting number? ')
num = range(int(n), int(m))
if n > m:
    print('Your starting number is larger than your ending number. ')
elif n <= m:
    print num

print ''

