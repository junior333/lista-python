#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do
#maior pelo menos valor.

a=int(input('digite o 1° valor: '))
b=int(input('digite o 2° valor: '))

if a>b:
    print(f'{a} - {b} = {a-b}')
else:
    print(f'{b} - {a} = {b-a}')