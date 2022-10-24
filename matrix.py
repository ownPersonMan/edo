from random import randint
n, m = 10, 10
matrix_1 = [[randint(-500, 500) for j in range(m)] for i in range(n)]
matrix_2 = [[randint(-500, 500) for j in range(m)] for i in range(n)]
print("Матрица 1: \n", matrix_1)
print("Матрица 2: \n", matrix_2)
result_sum=[[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
print("Сложение матриц:\n", result_sum)

