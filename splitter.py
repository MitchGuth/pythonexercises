def split(sentence):
    words = []
    padded_sentence = sentence.lower() + ''
    curr_word = ''
    for char in padded_sentence:
        if char == ' ':
            words.append(curr_word)
            curr_word = ''
        elif char == '.' or char == '!' or char == '?':
            words.append(curr_word)
            curr_word = ''
        else:
            curr_word += char
        return words

words = split(sentence)