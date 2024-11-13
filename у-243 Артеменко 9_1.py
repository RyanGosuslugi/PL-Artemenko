#Вариант 9 Заданние 1
from random import*

m=[]
n=int(input('Ввести число строк и столбцов квадратной матрицы: '))
k=int(input('Ввести число k: '))
m=([[randint(1,9) for j in range(n)] for i in range(n)])
c=0

print()
print('Матрица:')
for i in range(n):
    for j in range(n):
        print (m[i][j], end=' ')
    print()

list=[]
for i in range(n):
    for j in range(n):
        if m[i][j]%k==0:
            c+=1
            list.append(m[i][j])
print()
print('Число элементов, кратных k - '+str(c)+', из которых '+str(max(list))+' является наибольшим')
