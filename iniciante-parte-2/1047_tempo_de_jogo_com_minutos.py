hora_in,min_in,hora_fim,min_fim = map(int,input().split())

if hora_in == hora_fim and min_in == min_fim:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    minutos_iniciais = (hora_in * 60) + min_in
    minutos_finais = (hora_fim * 60) + min_fim
    if minutos_iniciais < minutos_finais:
        duracao_min = minutos_finais - minutos_iniciais
        horas = duracao_min // 60
        minutos_totais = duracao_min % 60
    else:
        duracao_min =  1440 - minutos_iniciais + minutos_finais
        horas = duracao_min // 60
        minutos_totais = duracao_min % 60
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos_totais} MINUTO(S)')