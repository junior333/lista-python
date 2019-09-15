#Receba 3 valores obrigatoriamente em ordem crescente e um 4o valor não
#necessariamente em ordem. Mostre os 4 números em ordem crescente.

a=int(input('digite o 1° valor: '))
b=int(input('digite o 2° valor: '))
c=int(input('digite o 3° valor: '))
d=int(input('digite o 4° valor: '))

if d<a:
    print(d,a,b,c)
elif d<b:
    print(a,d,b,c)
elif d<c:
    print(a,b,d,c)
else:
    print(a,b,c,d)