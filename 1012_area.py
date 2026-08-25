A,B,C = map(float,input().split())

area_tri = A * C/2
area_circ = 3.14159 * (C**2)
area_trapezio = (A + B) * C/2
area_quadr = B**2
area_ret = A * B

print(f'TRIANGULO: {area_tri:.3f}\nCIRCULO: {area_circ:.3f}\nTRAPEZIO: {area_trapezio:.3f}\nQUADRADO: {area_quadr:.3f}\nRETANGULO: {area_ret:.3f}')