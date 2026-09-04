x1,y1 = map(float, input().split())
x2,y2 = map(float, input().split())

dist = (x2 - x1)**2 + (y2 - y1)**2
distancia = dist**0.5
print(f'{distancia:.4f}')
