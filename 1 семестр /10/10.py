with open('Артеменко_Никита_У-243_vvod.txt', 'r') as file:
    lines=file.readlines()

m=[]
for line in lines:
    p=line.replace('[', '').replace(']', '').replace(',', '').strip()
    if p:
        row=list(map(int, p.split()))
        m.append(row)

k=int(input('Ввести число k: '))

c=0
list_1=[]
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]%k==0:
            c+=1
            list_1.append(m[i][j])

list_2=[]
for i in range(len(m)):
    for j in range(len(m[i])):
        list_2.append(abs(m[i][j]))
mx=max(list_2)

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]==mx:
            str_=i
            stolb=j
m.pop(str_)
for i in range(len(m)):
    m[i].pop(stolb)

with open('Артеменко_Никита_У-243_vivod.txt', 'w', encoding='utf-8') as file:
    file.write(f'Число элементов, кратных k - {c}, из которых {max(list_1)} является наибольшим \n\n')
    file.write('Матрица порядка n-1: \n')
    for row in m:
        file.write(f'{row} \n')
