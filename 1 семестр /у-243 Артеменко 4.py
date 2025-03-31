N=int(input("Введите количество чисел "))
fst=0
snd=1
dop=0
for i in range(N):
    print(snd, end=' ')
    dop=fst
    fst=snd
    snd+=dop
    