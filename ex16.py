#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual
#de desconto e o número de descendentes. Calcule o salário que serão as
#horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário
#Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário
#Líquido. Exiba o salário a receber.

ht=int(input('digite a quantidade de horas trabalhadas: '))
vh=int(input('digite o valor por hora: '))
pd=float(input('digite o porcentual de desconto: '))
ndesc=int(input('digite o numero de descendentes: '))
salarioBruto=int(ht*vh)
salarioLiquido=int(salarioBruto*(1-pd/100))
salarioReceber=int(salarioLiquido+100*ndesc)
print(f'o salario total a receber é {salarioReceber}')