valor = int(input()) 

n100 = valor // 100
valor1 = valor % 100

n50 = valor1 // 50
valor2 = valor1 % 50

n20 = valor2 // 20
valor3 = valor2 % 20

n10 = valor3 // 10
valor4 = valor3 % 10

n5 = valor4 // 5
valor5 = valor4 % 5

n2 = valor5 // 2
valor6 = valor5 % 2
n1 = valor6 // 1

print(valor)
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')