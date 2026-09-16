def calcular_quadrados (n):
    lista = list(range(1,n + 1))
    pares_ao_quadrado = []
    for i in lista:
        if i % 2 == 0:
            pares_ao_quadrado.append(f'{i}² = {i ** 2}')
    return '\n'.join(pares_ao_quadrado)
    
n = int(input())
res = calcular_quadrados(n)
print(res)