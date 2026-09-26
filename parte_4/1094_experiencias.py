def calcular_percentual(total,coelho,rato,sapo):
    
    percentual_coelho = ((sum(coelho))/total) * 100
    percentual_rato = ((sum(rato))/total) * 100
    percentual_sapo = ((sum(sapo))/total) * 100
    
    return f'Percentual de coelhos: {percentual_coelho:.2f} %\nPercentual de ratos: {percentual_rato:.2f} %\nPercentual de sapos: {percentual_sapo:.2f} %'
    

casos_teste = int(input())
sapos = []
coelhos = []
ratos = []
total = 0

for i in range(casos_teste):
    quantia, tipo = input().split()
    quantia = int(quantia)
    tipo = str(tipo).upper()
    
    if tipo == 'C':
        coelhos.append(quantia)
        total += quantia
        
    elif tipo == 'R':
        ratos.append(quantia)
        total += quantia
    else:
        sapos.append(quantia)
        total += quantia
        
percentual = calcular_percentual(total,coelhos,ratos,sapos)

print(f'Total: {total} cobaias\nTotal de coelhos: {sum(coelhos)}\nTotal de ratos: {sum(ratos)}\nTotal de sapos: {sum(sapos)}')
print(percentual)