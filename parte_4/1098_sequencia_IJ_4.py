for i in range(0,21,2):
    i_real = i/10
    for f in range(1,4):
        j_real = i_real + f
        
        if i % 10 == 0:
            print(f'I={int(i_real)} J={int(j_real)}')
        else:
            print(f'I={i_real:.1f} J={j_real:.1f}')