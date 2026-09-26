def seis_num_impares_consecutivos (x):
    encontrados = []
    i = 0
    while i < 6:
        if x % 2 != 0:
            encontrados.append(x)
            i += 1
        x += 1
       
    return encontrados

x = int(input())
res = seis_num_impares_consecutivos(x)
for i in res:
    print(i)