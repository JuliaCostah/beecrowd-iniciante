A,B,C = map(float,input().split())

if (B + C) > A and (A + C) > B and (A + B) > C:
    perimetro = A + B + C
    print(f'Perimetro = {perimetro:.1f}')
else: 
    area_trapezio = ((A + B) * C)/2
    print(f'Area = {area_trapezio:.1f}')