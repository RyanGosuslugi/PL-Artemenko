def find_max():
    n=int(input("Введите число: "))
    if n==0:
        return 0
    mx=find_max()
    return max(n, mx)


print("Наибольшее число в последовательности:", find_max())
