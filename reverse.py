message = 'hello world'

def reverse(message): 
    temp = list(message)
    print temp(range(0, len(message), -1))

reverse(message)
