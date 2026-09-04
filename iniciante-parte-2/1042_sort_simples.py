n1,n2,n3 = map(int,input().split())
ordem_inicial = f'{n1}\n{n2}\n{n3}'

if n1 < n2 and n1 < n3:
    menor = n1
    if n2 < n3:
        meio = n2
        maior = n3
    else:
        meio = n3
        maior = n2
elif n2 < n1 and n2 < n3:
    menor = n2
    if n1 < n3:
        meio = n1
        maior = n3
    else:
        meio = n3
        maior = n1  
else: 
    menor = n3
    if n1 < n2:
        meio = n1
        maior = n2
    else: 
        meio = n2
        maior = n1

print(f'{menor}\n{meio}\n{maior}')
print(f'\n{ordem_inicial}')