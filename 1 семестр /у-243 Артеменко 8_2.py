#Вариант 9 Задание 2
from random import*
def pro(n):
    c=1
    for i in n:
        c*=i
    return c

def sr_ar(n):
    c=0
    for i in n:
        c+=i
    return c/len(n)

m1=[randint(1,10) for i in range(randint(3,10))]
m2=[randint(1,10) for i in range(randint(3,10))]
m3=[randint(1,10) for i in range(randint(3,10))]
print('Первый массив:',m1)
print('Произведение элеменов первого массива равно '+str(pro(m1))+', а их среднее арифметическое -','{:.2f}'.format(sr_ar(m1)))
print()
print('Второй массив:',m2)
print('Произведение элеменов второго массива равно '+str(pro(m2))+', а их среднее арифметическое -','{:.2f}'.format(sr_ar(m2)))
print()
print('Третий массив:',m3)
print('Произведение элеменов третьего массива равно '+str(pro(m3))+', а их среднее арифметическое -','{:.2f}'.format(sr_ar(m3)))