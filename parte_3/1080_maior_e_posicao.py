def maior_e_posicao(lista):
    
    maior = max(lista)
    posicao = lista.index(maior) + 1
    
    return f'{maior}\n{posicao}'


num = []
for i in range(100):
    n = int(input())
    num.append(n)

res = maior_e_posicao(num)
print(res)