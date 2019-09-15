#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética.Mostre a mensagem de acordo com a média:
#a. Se a média for >= 6,0 exibir “APROVADO”;
#b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
#c. Se a média for < 3,0 exibir “RETIDO”.

n1=float(input('digite a 1ª nota: '))
n2=float(input('digite a 2º nota: '))
n3=float(input('digite a 3° nota; '))
n4=float(input('digite a 4° nota; '))

media=(n1+n2+n3+n4)/4
print(f'media = {media}')
if media>=6:
    print('aprovado')
elif media>=3:
    print('exame')
else:
    print('retido')