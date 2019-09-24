#Receba um número inteiro. Calcule e mostre o seu fatorial.

n=int(input('digite um numero: '))
f=int(n)

while n>1:
    n-=1
    print(f'{f} X {n} = {f*n}')
    f=f*n
print(f'fatorial = {f}')