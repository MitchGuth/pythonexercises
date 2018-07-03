phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}
print phonebook_dict['Elizabeth']
phonebook_dict['Kareem'] = '938-489-1234'
print phonebook_dict
del phonebook_dict['Alice']
print phonebook_dict
phonebook_dict['Bob'] = '968-345-2345'
print phonebook_dict

print ''
print ''


ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print ramit['email']
print ramit['interests'][0]
print ramit['friends'][0]['email']
print ramit['friends'][1]['interests'][1]

ramit['friends'][1] = {
    'name': 'Brandon',
    'email': 'example@gmail.com',
    'interests': ['coding', 'ping pong']
}
# for key in ramit:
#     for value in range(len(key)):

word_input = raw_input('Please give me a word: ')
word = word_input.lower()
print word
r = {}
total = 0

for char in word: 
    if char not in r:
        r[char] = total
        r[char] += 1
    elif char in r:
        r[char] += 1
print r

print ''
print ''

sentence_input = raw_input('Riddle me a sentance please: ')
sentence = sentence_input.lower()
words = []
wordlower = ''
d = {}


 
for char in range(len(sentence)):
    if char == 0:
        wordlower += sentence[char]
        if sentence[char + 1] == ' ':
            words.append(wordlower)
            wordlower = ''
    elif sentence[char] != ' ': 
        wordlower += sentence[char]
        if sentence[char] == '.':
            break
        elif sentence[char + 1] == ' ' or sentence[char + 1] == '.':
            words.append(wordlower)
            wordlower = ''
    elif sentence[char] == '.':
        break
        
print words

for item in words: 
    if item not in d:
        d[item] = 1
    elif item in d: 
        d[item] += 1
print d



# for char in word: 
#     if char not in r:
#         r[char] = total
#         r[char] += 1
#     elif char in r:
#         r[char] += 1
# print r

msg_input = raw_input("Sentence? ")
dict1 = {}
dict2 = {}
word = ''
list2 = ['!', '.', '?']
msg = msg_input.lower()

for char in range(len(msg)):
    if char == 0:
        word += msg[char]
        if msg[char + 1] == ' ':
            if word not in dict1: 
                dict1[word] = 1
                word = ''
            elif word in dict1:
                dict1[word] += 1
                word = ''
    elif msg[char] in list2:
        if word not in dict1: 
                dict1[word] = 1
                word = ''
        elif word in dict1:
                dict1[word] += 1
                word = ''
        break
    elif msg[char] != ' ' or char == len(msg):
        word += msg[char]
        if msg[char] == ' ':
            break
        elif msg[char + 1] == ' ' or char == len(msg):
            if word not in dict1: 
                dict1[word] = 1
                word = ''
            elif word in dict1:
                dict1[word] += 1
                word = ''
    elif msg[char] == ' ' and char == len(msg):
        break

print dict1



