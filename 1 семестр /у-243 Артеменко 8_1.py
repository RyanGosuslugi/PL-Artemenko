#Вариант 9 Заданние 1
def sum(x):
    c=0
    while x>0:
        c+=x%10
        x//=10
    return c

num=int(input('Ввести число '))
count=0

while num>0:
    num-=sum(num)
    if num>0:
        count+=1
print(count)
