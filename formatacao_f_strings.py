"""
Formatação basica de strings

s - string

d e i - int
f - float
x e X - hexadecimal (abcdef0123456789)

> - esquerda
< - direita
^ - centro


mesma coisa que format e f-strings
"""

variavel = 'abc'

print(f'{variavel:=>10}')
print(f'{variavel:=<10}')
print(f'{variavel:0^10}')
print(f'{1000.3456789:-,.2f}')
print(f'{1000.3456789:+,.2f}')
print(f'{-1000.3456789:-,.2f}')
print(f'O hexadecimal de 1500 é: {1500:08x}')
print(f'{variavel!r}')









