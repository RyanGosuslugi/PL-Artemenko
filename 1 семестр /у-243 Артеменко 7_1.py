#Вариант 9 Заданние 1

N=int(input('Ввести число элементов '))
m=[float(input('Ввести элемент ')) for i in range(N)]
num_min=min(m)

for i in m:
    if abs(i)<num_min:
        num_min=i
print(num_min,'(модуль равен '+ str(abs(num_min))+')')
m.reverse()
print(m)