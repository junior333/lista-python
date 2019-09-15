#Receba a hora de início e de final de um jogo (HH,MM) sabendo que o
#tempo máximo é de 24 horas e pode começar num dia e terminar noutro.

hi=int(input('digite a hora do inicio do jogo: '))
mi=int(input('digite os minutos iniciais do jogo: '))
hf=int(input('digite a hora final do jogo: '))
mf=int(input('digite os minutos finais do jogo: '))


if mf>mi:
    if hf>hi:
        hj=hf-hi
        mj=mf-mi
    else:
        hj=hf+24-hi
        mj=mf-mi
else:
    if hf<hi:
        hj=hf+24-hi
        mj=mf+60-mi
    else:
        hj=hf-1-hi
        mj=mf+60-mi

if hj<0:
    hj+=24

if mj<0:
    mj+=60

print(f'o horario do termino do jogo é {hj}h e {mj}min')