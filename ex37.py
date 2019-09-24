#Receba 100 números inteiros reais. Verifique e mostre o maior e o menos
#valor. Obs.: somente valores positivos.
from random import uniform

r=(uniform(0,100))
maior=r
menor = r
c=int(1)
while c<=99:
    r=(uniform(0,100))
    print(r)
    if r>maior:
        maior=r
    elif r<menor:
        menor=r
    c+=1
print(f'+{maior} -{menor}')
