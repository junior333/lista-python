# dissecando uma variável

var=input('digite algo: ')

print(f'{var} é {type(var)}')
print(f'{var} tem só espaços? {var.isspace()}')
print(f'{var} é numérico?? {var.isnumeric()}')
print(f'{var} é alfabetico? {var.isalpha()}')
print(f'{var} é alfanumerico? {var.isalnum()}')
print(f'{var} é só maiúsculas? {var.isupper()}')
print(f'{var} é só minúsculas? {var.islower()}')
print(f'{var} é título? {var.istitle()}')
print(f'como é {var} capitalizada? {var.capitalize()}')
