
n = int(input())
for b in range(n):
    soma = 0
    x,y = map(int,input().split())
    if x < y:
        for i in range(x + 1,y,1):
            if i % 2 != 0:
                soma += i
    elif x == y:
        soma = 0
    else:
         for i in range(x - 1,y,-1):
            if i % 2 != 0:
                soma += i  
                      
    print(f'{soma}') 