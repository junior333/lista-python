# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e
# mostre o resultado da somatória dos números ímpares entre esses valores.

n1 = int(input('digite o 1 numero: '))
n2 = int(input('digite o 2 numero: '))
somai = int(0)
if n1 > n2:
    print(f'{n1} é maior que {n2}')
    while n1 > n2:
        if n1 % 2 == 1:
            print(f'{n1}+')
            somai += n1
        n1 -= 1
else:
    print(f'{n2} é maior que {n1}')
    while n1 < n2:
        if n2 % 2 == 1:
            print(f'{n2}+')
            somai += n2
        n2 -= 1
print(f'={somai}')