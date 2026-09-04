nome = input().upper()
sal = float(input())
vendas_mes = float(input())

total = sal + (vendas_mes * 0.15)
print(f'TOTAL = R$ {total:.2f}')
