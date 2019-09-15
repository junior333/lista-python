#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

a=int(input('digite o 1° numero'))
b=int(input('digite o 2° numero'))

if a<b:
    if b%a==0:
        print('o maior numero é multiplo do menor')
    else:
        print('o maior numero não é multiplo do menor')
else:
    if a%b==0:
        print('o maior numero é multiplo do menor')
    else:
        print('o maior numero não é multiplo do menor')