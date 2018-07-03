lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

example = "hello"
placeholder = ''
new_string= ''

for char in example: 
    for j in range(len(lowercase)):
        if char in lowercase:
            if char == str(lowercase[j]):
                placeholder = lowercase[j]
                new_string += str(uppercase[j])
                break
        else:
            new_string += char

print new_string

print ''
print ''

# question 2
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

statement = "hello. friend. how. are. you?"
placeholder = ""
new_string= ""

for char in range(len(statement)):
    for i in range(len(lowercase)):
        if  statement[char] == statement[0]:
            if statement[char] == str(lowercase[i]):
                placeholder = lowercase[i]
                new_string += str(uppercase[i])
                break
        elif statement[char-1] == " ":
            if statement[char] == str(lowercase[i]):
                placeholder = lowercase[i]
                new_string += str(uppercase[i])
                break
        else:
            new_string += statement[char]
            break

print new_string

print ''
print ''

lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

statement = "hello. friend. how. are. you?"
temp = ""
new_string= ""

for i in range(len(statement)):
    if i == 0:
        if statement[i] in lowercase:
            temp = lowercase.index(statement[i])
            new_string += uppercase[temp]
            
        else:
            new_string += statement[i]
            
    elif statement[i-1] == " ":
        if statement[i] in lowercase:
            temp = lowercase.index(statement[i])
            new_string += uppercase[temp]
            
        else: 
            new_string += statement[i]
            
    else:
        new_string += statement[i]
        

print new_string

# question #3

message = "sample message"

total = len(message)
print message[:: -1]


# question 4

text = "Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements"
list1 = ["A", "E", "G", "I", "O", "S", "T"]
list2 = ["4", "3", "6", "1", "0", "5", "7"]
new_text= ""

for char in text.upper():
    if char in list1: 
        for j in range(len(list1)):
            if char == list1[j]:
                new_text += list2[j]
                break
    else:
        new_text += char
print new_text