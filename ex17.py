#Calcule a quantidade de litros gastos em uma viagem, sabendo que o
#automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

tp=int(input('digite o tempo do percurso: '))
vm=int(input('digite a velocidade media: '))

print(f'a quantidade de litros gastos é {tp*vm/12}')