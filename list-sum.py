num = [1, 2, 3, 4]
print sum(num)

print ''

numlist = [7, 2, 3, 4]
greatest = 0
for i in numlist :
    if i > greatest:
        greatest = i
        print i

print ''

examplelist = [8, 4, 3, 7]
least = 100
for i in examplelist:
    if i < least:
        least = i
print least

print ''

evenlist = [4, 6, 9, 3]
for i in evenlist:
    if i % 2 == 0:
        print i

print ''

poslist = [-8, -3, 4, 2]
for i in poslist:
    if i > 0:
        print i

print ''

oldlist = [-8, -3, 4, 2]
newlist = []
for i in oldlist:
    if i > 0:
        newlist.append(i)
        print newlist

        
        