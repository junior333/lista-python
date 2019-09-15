larg=float(input('digite a largura da parede(mts): '))
alt=float(input('digite a altura da parede(mts): '))

#cada litro de tinta cobre 2m²

print(f'numa área de {larg*alt:.2f}² o total de tinta necessária é {larg*alt/2:.2f} litros')
