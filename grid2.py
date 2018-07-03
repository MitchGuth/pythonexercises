height = raw_input('How high would you like your rectangle? ')
width = raw_input('How wide would you like your rectangle? ')
height = int(height)
width = int(width)

height_range = range(1, height + 1)
width_range = range(1, width + 1)

box = 1

for box in height_range:
    if (box == 1 or box == height):
        print ('*' * width)
    else:
        print ('*' + (" " * (width - 2)) + '*')
    box += 1
            
print ""

height = int(raw_input("How tall would you like your triangle? "))
height_range = range(0, height)
number_stars = 1

for element in height_range:
    while number_stars <= height: 
        print ((" " * ((number_stars + height) - 4)) + ("*" * number_stars) + " " * ((number_stars - height) - 4))
        number_stars += 2




