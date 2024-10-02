n, m, k = map(int, input().split())
c=False
for i in range(1, n + 1):
    if m * i == k:
        c = True
        break

for j in range(1, m + 1):
    if n * j == k:
        c = True
        break

if c == True:
    print('да')
else:
    print('нет')