message = 'you shall NOT pass'
upcased = ''
letter_mapping = {
    'a':'A',
    'b':'B',
    'c':'C',
    'd':'D',
    'e':'E',
    'f':'F',
    'g':'G',
    'h':'H',
    'i':'I',
    'j':'J',
    'k':'K',
    'l':'L',
    'm':'M',
    'n':'N',
    'o':'O',
    'p':'P',
    'q':'Q',
    'r':'R',
    's':'S',
    't':'T',
    'u':'U',
    'v':'V',
    'w':'W',
    'x':'X',
    'y':'Y',
    'z':'Z'
}
for char in message:
    letter = char
    # search the list of lowercase letters
    if char in letter_mapping:
        letter = letter_mapping[char]

        upcased = upcased + letter

print upcased


print ''
print ''

sentence = 'to be or not to be'
# there be magic! It took sentance and made it into a list of words
words = []
word_count = {}
padded_sentence = sentence + ''
curr_word = ''

for char in padded_sentence:
    if char == ' ':
        words.append(curr_word)
        curr_word = ''
    else:
        curr_word += char

for word in words:
    if word in word_count:
        word_count[word] += 1
    else :
        word_count[word] = 1

print word_count
