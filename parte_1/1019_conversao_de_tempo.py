s = int(input())
horas = s//3600
minutos = (s % 3600) // 60
segundos = abs((minutos * 60) - (s % 3600))

print(f'{horas}:{minutos}:{segundos}')