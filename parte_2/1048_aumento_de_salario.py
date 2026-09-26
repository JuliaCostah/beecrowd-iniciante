sal_inicial = float(input())

if 0 <= sal_inicial <= 400.00:
    reajuste = sal_inicial * 0.15
    sal_final = sal_inicial + reajuste
    print(f'Novo salario: {sal_final:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}\nEm percentual: 15 %')
elif sal_inicial <= 800.00:
    reajuste = sal_inicial * 0.12
    sal_final = sal_inicial + reajuste
    print(f'Novo salario: {sal_final:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}\nEm percentual: 12 %')
elif sal_inicial <= 1200.00:
    reajuste = sal_inicial * 0.10
    sal_final = sal_inicial + reajuste
    print(f'Novo salario: {sal_final:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}\nEm percentual: 10 %')
elif sal_inicial <= 2000.00:
    reajuste = sal_inicial * 0.07
    sal_final = sal_inicial + reajuste
    print(f'Novo salario: {sal_final:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}\nEm percentual: 7 %')
else:
    reajuste = sal_inicial * 0.04
    sal_final = sal_inicial + reajuste
    print(f'Novo salario: {sal_final:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}\nEm percentual: 4 %')