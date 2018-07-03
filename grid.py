grid = 5
for i in range(grid):
    print ('*' * grid)

print ''

user_input = raw_input('How big would you like the square? ')
user_input = int(user_input)
for i in range(user_input):
    print ('*' * user_input)

print ''

def hollow_rect(height, width):
    for i in range(1, height+1):
        for j in range(1, width+1):
            if (i == 0 or i == h or j == 0 or j == w):
                print ('*', '')
            else:
                print ('', '')

height = raw_input('How high would you like your rectangle? ')
width = raw_input('How wide would you like your rectangle? ')
height = int(h)
width = int(w)
        
print hollow_rect(h, w)

