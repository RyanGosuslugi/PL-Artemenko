#Вариант 9 Задание 2
from random import*

m=[]
n=int(input('Ввести число строк и столбцов квадратной матрицы: '))
m=([[randint(1,20) for j in range(n)] for i in range(n)])

list=[]
print()
print('Матрица порядка n:')
for i in range(n):
    for j in range(n):
        print ('{:3d}'.format(m[i][j]), end=' ')
        list.append((abs(m[i][j])))
    print()

print()
print('Наибольший по модулю элемент:',max(list))    
print()

for i in range(n):
    for j in range(n):
        if m[i][j]==max(list):
            str_=i
            stolb=j
m.pop(str_)
for i in range(len(m)):
    m[i].pop(stolb)

print('Матрица порядка n-1:')    
for i in range(len(m)):
    for j in range(len(m)):
        print ('{:2d}'.format(m[i][j]), end=' ')
    print()
