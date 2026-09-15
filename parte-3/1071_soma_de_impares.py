def soma_impares_consecutivos (x,y):
    soma = 0
    menor = min(x,y)
    maior = max(x,y)
    for i in range(menor + 1,maior):
        if i % 2 != 0:
            soma += i
    return soma

x = int(input())
y = int(input())
res = soma_impares_consecutivos(x,y)
print(res)