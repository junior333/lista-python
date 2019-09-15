#Receba 2ângulos de um triângulo. Calcule e mostre o valor do 3o ângulo.

a= int(input('digite o primeiro angulo: '))
b=int(input('digite o segundo angulo: '))
if a+b<180:
    print(f'o valor o terceiro angulo é {180-a-b}')
else:
    print('angulos inválidos')