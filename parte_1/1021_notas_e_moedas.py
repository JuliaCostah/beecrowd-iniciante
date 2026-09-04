valor = float(input())
centavos = int(round(valor * 100))

#Notas
n100 = centavos // 10000
centavos = centavos % 10000
n50 = centavos // 5000
centavos = centavos % 5000
n20 = centavos // 2000
centavos = centavos % 2000
n10 = centavos // 1000
centavos = centavos % 1000
n5 = centavos // 500
centavos = centavos % 500
n2 = centavos // 200
centavos = centavos % 200

#Moedas
m1 = centavos // 100
centavos = centavos % 100
m050 = centavos // 50
centavos = centavos % 50
m025 = centavos // 25
centavos = centavos % 25
m010 = centavos // 10
centavos = centavos % 10
m005 = centavos // 5
centavos = centavos % 5
m001 = centavos // 1

print('NOTAS:')
print(f'{n100:.0f} nota(s) de R$ 100.00')
print(f'{n50:.0f} nota(s) de R$ 50.00')
print(f'{n20:.0f} nota(s) de R$ 20.00')
print(f'{n10:.0f} nota(s) de R$ 10.00')
print(f'{n5:.0f} nota(s) de R$ 5.00')
print(f'{n2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{m1:.0f} moeda(s) de R$ 1.00')
print(f'{m050:.0f} moeda(s) de R$ 0.50')
print(f'{m025:.0f} moeda(s) de R$ 0.25')
print(f'{m010:.0f} moeda(s) de R$ 0.10')
print(f'{m005:.0f} moeda(s) de R$ 0.05')
print(f'{m001:.0f} moeda(s) de R$ 0.01')