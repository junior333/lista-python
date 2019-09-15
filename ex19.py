#Receba 2 valores reais. Calcule e mostre o maior deles.

a=int(input('digite o 1° valor: '))
b=int(input('digite o 2° valor: '))

if a>b:
    print(f'{a}>{b}')
else:
    print(f'{b}>{a}')