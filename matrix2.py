# first_matrix = [[7, 9], [4, 8]]
# second_matrix = [[1, 4], [6, 2]]
# sum_matrix = []

# for i in range(len(first_matrix)):
#     sum_matrix.append([])
#     for j in range(len(first_matrix[0])):
#         sum_matrix[i].append(first_matrix[i][j] + second_matrix[i][j])
# print sum_matrix


# simple matrix addition
def create_empty_matrix(width, height):
    result = []
    for i in range(0, height):
        result.append([])
        for j in range(0, width):
            result[i].append(0)
    return result

def add_matrices(m1, m2):
    matrix = create_empty_matrix(width, height)
    height = len(m1)   
    width = len(m1[0])
    for i in range(0, height):
        for j in range(0, width):
            cell1 = m1[i][j]
            cell2 = m2[i][j]

            matrix[i][j] = cell1 + cell2
    return matrix

m1 = [[1, 4], [5, 8]]
m2 = [[8, 2], [3, 1]]

add_matrices(m1, m2)

result = matrix

print result
