cod, quant = map(int,input().split())

if cod == 1:
    preco = 4.00
    total = quant * preco
    print(f'Total: R$ {total:.2f}')
elif cod == 2:
    preco = 4.50
    total = quant * preco
    print(f'Total: R$ {total:.2f}')
elif cod == 3:
    preco = 5.00
    total = quant * preco
    print(f'Total: R$ {total:.2f}')
elif cod == 4:
    preco = 2.00
    total = quant * preco
    print(f'Total: R$ {total:.2f}')
else:
    preco = 1.50
    total = quant * preco
    print(f'Total: R$ {total:.2f}')