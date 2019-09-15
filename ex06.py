#Receba os valores em x e y. Efetua a troca de seus valores e mostre seus
#conteúdos.

x=int(input('digite o valor x: '))
y=int(input('digite o valor y: '))
aux=int(x)
x=y
y=aux
print(f'x={x} e y={y}')