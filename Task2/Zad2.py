def shortest_way(matrix, size):
    for i in range(size):
        for j in range(size):
            if i == j == 0:
                pass
            elif i > 0 and j == 0:
                matrix[i][j] += matrix[i - 1][j]
            elif i == 0 and j > 0:
                matrix[i][j] += matrix[i][j - 1]
            else:
                if matrix[i - 1][j] < matrix[i][j - 1]:
                    matrix[i][j] += matrix[i - 1][j]
                else:
                    matrix[i][j] += matrix[i][j - 1]
    return A[size-1][size-1]


print("please insert name of the file: ")
name = input()+".txt"
file_object = open(name, 'r')
A = []

while True:
    tmp = file_object.readline()
    if tmp == ("" or "\n"):
        break
    size_of_matrix = int(tmp)
    for iterator in range(size_of_matrix):
        A.append([int(x) for x in file_object.readline().split(',')])
    print(shortest_way(A, size_of_matrix))
    A = []
