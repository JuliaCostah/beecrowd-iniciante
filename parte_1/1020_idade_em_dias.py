idade_dias = int(input()) 

anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = abs((meses * 30) - (idade_dias % 365))

print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')