"""
Interpolação basica de strings
s - string

d e i - int
f - float
x e X - hexadecimal (abcdef0123456789)

mesma coisa que format e f-strings
"""



nome = 'sivaldo'
preco = 1000.9776543

variavel = '%s, o preco total foi R$ %.2f ' % (nome, preco)

print(variavel)

print('O hexadecimal de %d é %04X' % (15, 15))









