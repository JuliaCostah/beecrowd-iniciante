while True:
    M,N = map(int,input().split())

    if M <= 0 or N <= 0:
        break
    
    menor = min(M,N)
    maior = max(M,N)
    soma = 0
    
    for i in range(menor,maior + 1,1):
        print(f'{i} ',end='')
        soma += i
    
    print(f'Sum={soma}')