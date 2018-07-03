#Given a paragraph of text as a string, print the paragraph in leetspeak. 
# To translate a string to leetspeak, you need to replace 
# make the following character replacements (treat all input characters as uppercase):
# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

def leet(paragraph):
    dict1 = {'A': '4', 'E': '3', 'G': '6', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}
    new_paragraph = ''
    for letter in paragraph: 
        upper = letter.upper()
        if upper in dict1:
            new_paragraph += dict1[upper]
        else: 
            new_paragraph += letter
    return new_paragraph
result = leet('Hello world')
print result

print ''
print ''

# def split(sentence):
#     words = []
#     padded_sentence = sentence.lower() + ''
#     curr_word = ''
#     for char in padded_sentence:
#         if char == ' ':
#             words.append(curr_word)
#             curr_word = ''
#         elif char == '.' or char == '!' or char == '?':
#             words.append(curr_word)
#             curr_word = ''
#         else:
#             curr_word += char
#         return words

# words = split(sentence)

import splitter # you could also import split by using: from splitter import split
#so you would not need to use splitter.split to call the function just split

words = splitter.split(sentence)

def wordsdict(words)  
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else :
            word_count[word] = 1

    return word_count


result = wordsdict(raw_input('Riddle me a sentence: '))
print result