# def alg(num):
#     sum = 0
#     for num in range(1000):
#         if num % 3 == 0 or num % 5 == 0:
#             sum += num 
#             num += 1
#         else:
#             num += 1
#     return sum

# result = alg(1)
# print result

# print ''
# print ''

# def alg2(num):
#     sum = 2
#     current = 3
#     sec = 2
#     first = 1
#     while current < num:
#         if current % 2 == 0: 
#             sum += current
#             first = sec
#             sec = current 
#             current = sec + first
            
#         else: 
#             first = sec
#             sec = current 
#             current = sec + first
#     return sum

# aha = alg2(4000000)

# print aha

# print ''
# print ''

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

    