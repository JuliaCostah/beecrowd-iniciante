sal_inicio = float(input())

if 0.00 <= sal_inicio <= 2000.00:
    print('Isento')
elif 2000.01 < sal_inicio <= 3000.00:
    imposto = (sal_inicio - 2000) * (8/100) # 1000 * 0,08 = 80,00
    print(f'R$ {imposto:.2f}')
elif 3000.01 < sal_inicio <= 4500.00:
    imposto = 80.00 + ((sal_inicio - 3000) * (18/100)) # 1500 * 0,18 = 270,00
    print(f'R$ {imposto:.2f}')
else:
    imposto = 350.00 + ((sal_inicio - 4500) * (28/100))
    print(f'R$ {imposto:.2f}')