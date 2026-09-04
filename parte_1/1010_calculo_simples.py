cod1,quant1,valor_unitario1 = input().split()
quant1,valor_unitario1 = int(quant1), float(valor_unitario1)
cod2,quant2,valor_unitario2 = input().split()
quant2,valor_unitario2 = int(quant2), float(valor_unitario2)


total = (quant1 * valor_unitario1) + (quant2 * valor_unitario2)
print(f'VALOR A PAGAR: R$ {total:.2f}')