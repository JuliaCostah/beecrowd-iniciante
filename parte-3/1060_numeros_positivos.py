positivos = []
for i in range(6):
    valores = float(input())
    if valores > 0:
        positivos.append(valores)
print(f'{len(positivos)} valores positivos')