def calculate_media_ponderada(n1,n2,n3):
    
    media = ((n1 * 2) + (n2 * 3) + (n3 * 5))/10
    
    return f'{media:.1f}'

test_cases = int(input())

for _ in range(test_cases):
        n1,n2,n3 = map(float,input().split())
        
        print(calculate_media_ponderada(n1,n2,n3))