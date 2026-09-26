pares = []

for i in range(5):
    n = int(input())
    if n % 2 == 0:
        pares.append(n)
print(f'{len(pares)} valores pares')