km=float(input('escreva a quantidade de quilometros rodados pelo carro: '))
dias=int(input('escreva a quantidade de dias em que o carro foi alugado: '))

print(f'{km} X RS 0,15/km')
print(f'{dias} X R$60,00/dia')
print(f'total {km * 0.15 + dias * 60}')