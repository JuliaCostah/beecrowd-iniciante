x = int(input())

lista = list(range(1,x + 1))
for x in lista:
    if x % 2 != 0:
        print(x)