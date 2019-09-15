# Receba o preço atual e a média mensal de um produto. Calcule e mostre o
# novo preço sabendo que:
# Venda Mensal        Preço Atual     Preço Novo
#  < 500               < 30              +10%
#  >= 500 e < 1000     >= 30 e < 80      +15%
#  >= 1000             >= 80             -5%
# Obs.: para outras condições, preço novo será igual ao preço atual.

mm = int(input('digite a media menssal do produto: '))
pa = int(input('digite o preço atual do produto: '))
pn = pa

if mm < 500 & pa < 30:
    pn = pa * 1.10
elif mm < 1000 :
    pn = pa * 1.15
elif mm >= 1000 :
    pn = pa * 0.95
else:
    print(f'condição não prevista, preço atual mantido')

print(f'novo preço do produto é R$ {pn}')
