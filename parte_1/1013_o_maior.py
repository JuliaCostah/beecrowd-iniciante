A,B,C = map(int,input().split())

maiorAB = (A + B + abs(A - B))/2

if maiorAB > C:
    print(f'{maiorAB:.0f} eh o maior')
else:
    print(f'{C:.0f} eh o maior')