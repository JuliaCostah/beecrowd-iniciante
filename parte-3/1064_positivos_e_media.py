num = []
for i in range(6):
    n = float(input())
    num.append(n)
    
positivos = []
for i in num:
    if i > 0.0:
        positivos.append(i)
        
media = sum(positivos)/len(positivos)
print(f'{len(positivos)} valores positivos')
print(f'{media:.1f}')