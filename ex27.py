#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de
#duração (minutos). Calcule e mostre a velocidade média em km/h.

vt=int(input('digite o numero de voltas: '))
ext=int(input('digite a extensão do percurso(metros): '))
tempo=int(input('digite o tempo de duração(min): '))

print(f'a velocidade média é {(vt*ext/1000)/(tempo/60)} kms/h')