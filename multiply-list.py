# mult_list = [4, 8 , 7 , 3]
# new_list = []
# factor = 9

# for i in mult_list: 
#     new_list.append(i * factor)
# print new_list

# print ''
# print ''


# first_list = [2, 4, 6]
# second_list = [3, 5, 7]
# combined_list = []

# for i in range(0, len(first_list)):
#     combined_list.append(first_list[i] * second_list[i])
    
# print combined_list

# print ''
# print ''

# difficult matrix addition

# first_matrix = [[7, 9], [4, 8]]
# second_matrix = [[1, 4], [6, 2]]
# sum_matrix = []

# for i in range(len(first_matrix)):
#     sum_matrix.append([])
#     for j in range(len(first_matrix[0])):
#         sum_matrix[i].append(first_matrix[i][j] + second_matrix[i][j])
# print sum_matrix

# print ''
# print ''

# # Still needs work!

# matrix1 = [1, 8, 2, 3, 3, 8, 9, 4, 3, 1, 5]
# new_matrix = []

# for i in range(len(matrix1)):
#     if i not in new_matrix:
#         new_matrix.append(matrix1[i])
# print new_matrix


# simple matrix addition

m1 = [[1, 4], [5, 8]]
m2 = [[8, 2], [3, 1]]
r = [[], []]

# for row in m1:
#     for col in row:

height = len(m1)   
width = len(m1[0])


for i in range(height):
    for j in range(width):
        r[i] = m1[i][j] + m2[i][j]
       