#Receba os coeficientes A, B e C de uma equação do 2o grau
#(AX2+BX+C=0). Calcule e mostre as raízes reais (considerar que a
#equação possue2 raízes).

a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))

d=int((b*b)-4*a*c)

if d>0:print(f'a primeira raíz é {(-b+(d**(1/2)))/2*a} e a segunda raiz é {(-b-(d**(1/2)))/2*a}')
else:print('raiz inválida')