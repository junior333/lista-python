mt=int(input('digite um valor em metros: '))

print('''{} kilometro(s)
{} hectometro(s)
{} decametro(s)
{} metro(s)
{} decimetro(s)
{} centimetro(s)
{} milimetro(s)'''.format(mt/1000,mt/100,mt/10,mt,mt*10,mt*100,mt*1000))