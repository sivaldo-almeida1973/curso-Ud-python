"""
Dict Comprehension

Represnentado por {}
Possuem a relacao chave->dado

como declarar?===================
A) Exemplo criar dicionario com idade pela metade de idade=============

pessoasIdade = {'Ana':25, 'Maria': 35}
pessoasMeiaIdade = {chave: dado // 2 for chave , dado in pessoasIdade.items()}  #--------

print(f"Lista Comprehension:",pessoasMeiaIdade)

#mesmo resultado com for =========================

pessoasMeiaIdade = {}  # declarar variavel
for chave,dado in pessoasIdade.items():## mesmo resulatdo de cima
  pessoasMeiaIdade[chave] = dado // 2

print(f"Com for",pessoasMeiaIdade)

B) Exemplo criar dicionario com apenas maiores de idade=============

pessoasIdade = {'Ana':25, 'Maria': 35, 'Lucas': 17}
MaiorIdade = {chave: dado for chave , dado in pessoasIdade.items() if dado >= 18}  #-------- se idade for maior que 18 chave recebe dado

print(f"Lista Comprehension:",MaiorIdade)

C)Exemplo com if,els e for:
#criar dicionario com maiores e, mascom aviso para menores

"""


pessoasIdade = {'Ana':25, 'Maria': 35, 'Lucas': 17}
MaiorIdade = {chave: (dado if dado >= 18 else 'não pode entrar') for chave, dado in pessoasIdade.items()}  #-------- 

print(f"Lista Comprehension:",MaiorIdade)

