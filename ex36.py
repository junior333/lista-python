#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

n=int(input('digite um valor: '))
s=int(1)
c=int(1)
print(f'{s}+')
while c<=n:
    f=c
    cf=1
    while cf<c:
        f*=cf
        cf+=1
    print(f'1/{f} = {1/f} +')
    s+=1/f
    c+=1
print(f'a serie é {s}')