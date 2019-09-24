#Receba um número. Calcule e mostre os resultados da tabuada desse número.

n=int(input('digite um numero'))
c=int(1)

while c<=10:
    print(f'{n}x{c}={n*c}')
    c+=1