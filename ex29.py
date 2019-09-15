# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do
# investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a
# poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

ti = int(input("digite o tipo de investimento: "))
valor = int(input("digite o valor de investimento: "))

if ti == 1:
    valor *= 1.03
    print(f'o valor corrigido é {valor}')
elif ti == 2:
    valor *= 1.05
    print(f'o valor corrigido é {valor}')
else:
    print('opção inválida digite novamente')

