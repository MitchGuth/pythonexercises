def sumlist(listofnumbers):
    total = 0
    for num in listofnumbers: 
        total += num
    return total

numlist = [9, 3, 4, 1, 6, 7, 5]
numlist2 = [1, 1, 2, 2]

print sumlist(numlist)
print sumlist(numlist2)

print ''
print ''

def largestnumber(givenlist):
    large = 0
    for num in givenlist:
        if num > large: 
            large = num
    return large

largelist1 = [8, 4, 1, 2, 9, 20]
largelist2 = [0, 3, 5, 2, 21, 7]

print largestnumber(largelist1)
print largestnumber(largelist2)

print ''
print ''

def evennumber(givenlist):
    evens = []
    for num in givenlist:
        if num % 2 == 0 and num != 0:
            evens.append(num)
    return evens

evenlist1 = [8, 4, 1, 2, 9, 20]
evenlist2 = [0, 3, 5, 2, 21, 7]

print evennumber(evenlist1)
print evennumber(evenlist2)

print ''
print ''

def posonly(givenlist):
    newlist = []
    for num in givenlist:
        if num > 0: 
            newlist.append(num)
    return newlist

abslist = [-1, 2, -3, 4, -5, 6, -7, 8]
print posonly(abslist)

print ''
print ''

def multfactor(givenlist, factor):
    newlist = []
    tempvalue = 0
    for num in givenlist:
        tempvalue = num * factor
        newlist.append(tempvalue)
    return newlist

examplelist = [1, 2, 3, 4, 5, 6]

print multfactor(examplelist, 5)

print ''
print ''

def multvector(givenlist1, givenlist2):
    newlist = []
    for num in range(0, len(givenlist1)):
        newlist.append(givenlist1[num] * givenlist2[num])
    return newlist

listm1 = [2, 4, 5] 
listm2 = [2, 3, 6]

print multvector(listm1, listm2)

print ''
print ''


def create_empty_matrix(width, height):
    result = []
    for i in range(0, height):
        result.append([])
        for j in range(0, width):
            result[i].append(0)
    return result

def add_matrices(m1, m2):
    height = len(m1)   
    width = len(m1[0])
    newmatrix = create_empty_matrix(width, height)
    for i in range(0, height):
        for j in range(0, width):
            cell1 = m1[i][j]
            cell2 = m2[i][j]
            newmatrix[i][j] = cell1 + cell2
    return newmatrix

m1 = [[1, 4], [5, 8]]
m2 = [[8, 2], [3, 1]]

variable = add_matrices(m1, m2)

print variable





