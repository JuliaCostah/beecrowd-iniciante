categoria = input().lower()
tipo1 = input().lower()
tipo2 = input().lower()

if categoria == 'vertebrado':
    if tipo1 == 'ave':
        if tipo2 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else: 
        if tipo2 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if tipo1 == 'inseto':
        if tipo2 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if tipo2 == 'onivoro':
            print('minhoca')
        else:
            print('sanguessuga')