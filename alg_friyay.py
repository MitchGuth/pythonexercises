def biggestprimefactor(giant):
    factor = 1
    while giant > factor:
        factor += 1
        while giant % factor == 0:
            giant = giant/factor
    return factor
giant = input('Give me a rediculously large integer: ')
value = biggestprimefactor(giant)
print value

# Johnathan's solution
number = 600851475143
remainder = number
factor = 2
while remainder != 1:
    if remainder % factor == 0:
        remainder /= factor
    else:
        factor += 1  
print factor

    