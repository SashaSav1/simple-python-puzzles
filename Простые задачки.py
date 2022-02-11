# Задание 1
# Выполнить обработку элементов прямоугольной матрицы A, имеющей N
# строк и M столбцов. Найти наименьший элемент столбца матрицы A, для
# которого сумма абсолютных значений элементов максимальна.
# Задание 2
# Задан список А[1..5,1..6]. Поменять в нем местами первый и последний
# столбец.
# Задание 3
# Найти номер строки и столбца максимального элемента двумерного списка
# целых чисел размерности 7*4

# Задание 4
# Заполнить двумерный список целыми числами от 1 до 100 по спирали
# Задание 5
# Имеется двумерный список целых чисел размерности 6*5. Найти номер
# строки, для которой среднеарифметическое значение ее элементов
# максимально.

#Задание 1

# N = int(input("Строки: "))
# M = int(input("Столбцы: "))

# A = []

# min_ = 10000
# max_ = 1
# summ = 0
# stolbec = 0

# for i in range(N):
# 	A1 = []
# 	for j in range(M):
# 		a = int(input())
# 		A1.append(a)
# 	A.append(A1)

# for i in range(M):
# 	summ = 0
# 	for j in range(N):
# 		summ += abs(A[j][i])
# 	if summ > max_:
# 		max_ = summ
# 		stolbec = i

# for i in range(N):
# 		if A[i][stolbec] < min_:
# 			min_ = A[i][stolbec]

# print("Мин: ", min_)

#Задание 2

# A = [[1,2,3],
# 	 [4,5,6]]

# a = A[0][0]
# b = A[0][2]
# c = A[1][0]
# d = A[1][2]

# A[0][0] = b
# A[0][2] = a
# A[1][0] = d
# A[1][2] = c

# print(A) 

#Задание 3

# N = 7
# M = 4

# max_ = 0

# stolbecMax_ = 0
# strokaMax_ = 0

# A = []

# for i in range(N):
# 	A1 = []
# 	for j in range(M):
# 		a = int(input())
# 		A1.append(a)
# 	A.append(A1)

# for i in range(N):
# 	for j in range(M):
# 		if A[i][j] > max_:
# 			max_ = A[i][j]
# 			stolbecMax_ = j
# 			strokaMax_ = i

# print("Максимальное число, его строка и столбец: ", max_, " ", strokaMax_, " ", stolbecMax_)

#Задание 4

# n = int(input())
# l = [[0 for j in range(n)] for i in range(n)]
# N = n*n
# i = 0
# j = 0
# k = 1
# while k <= N:
#     l[i][j] = k
#     if i <= j + 1 and i + j < n - 1: 
#         j += 1
#     elif i < j and i + j >= n-1: 
#         i += 1
#     elif i >= j and i + j > n-1: 
#         j -= 1
#     else: 
#         i -= 1
#     k += 1
 
 
# for i in l:
#     print(*i,sep='\t')

#Задание 5
# N = 6
# M = 5

# summ = 0
# max_ = 0
# strokaMax_ = 0

# A = []

# for i in range(N):
# 	A1 = []
# 	for j in range(M):
# 		a = int(input())
# 		A1.append(a)
# 	A.append(A1)

# for i in range(N):
# 	summ = 0
# 	for j in range(M):
# 		summ += A[i][j]
# 	summ /= M
# 	if (summ) > max_:
# 		max_ = summ
# 		strokaMax_ = i

# print(A)

# print("Номер строки у которой среднеарифметическое большее: ", strokaMax_)



