def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list2 = []
        matrix.append(list2)
        for j in range(m):
            list2.append(value)
    return matrix

result1 = get_matrix(2, 5, 11)
result2 = get_matrix(7, 2, 25)
result3 = get_matrix(3, 4, 30)
print(result1)
print(result2)
print(result3)



