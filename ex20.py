#Receba 3 coeficientes A, B, e C de uma equação do 2o grau da fórmula
#AX2+BX+C=0. Verifique e mostre a existência de raízes reais e se caso
#exista, calcule e mostre.

a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))

d=int((b*b)-4*a*c)

if d>0:print(f'a primeira raíz é {(-b+(d**(1/2)))/2*a} e a segunda raiz é {(-b-(d**(1/2)))/2*a}')
else:print('raiz inválida')