#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

n=int(input('digite um numero: '))
c=int(1)
s=int(0)

while c<=n:
    print(f'1/{c}+')
    s+=1/c
    c+=1
print(f'={s}')