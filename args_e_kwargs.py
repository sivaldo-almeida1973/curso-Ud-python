"""
*args = Gera uma tupla
 ** kwargs = gera um dicionario

-sao parametros como quaisquer outros
-sao obrigatorios (não exigem orgumentos)
-seus nomes não importam, e sim os asterico(s) # *batata , **bode
-args  kwargs- sao apenas por convenção
-ajudam a evitar erros, e tornam a funcao mais dinamica

#Ex:
def cadastro(nome, idade, *args):
  print(f'Nome: {nome}')
  print(f'Idade: {idade}')
  print(f'Profissão: ', end=' ')
  for prof in args:
    print(prof, end=',')

cadastro('Anganldo', 67, 'carpinteiro','montador', 'marcineiro')

=====================================
#exemplo 2:

def media(*args):
  print(args)
  print(sum(args)/len(args))

media(1,2,3,4,5,6)

=========================================
def media(peixe, num, *args):
  print(args)
  print(sum(args)/len(args))

media(1,2,3,4,5,6)

=============================================

#Exemplo 3:
notas = [8,9,7,10,23,45,33,15,24,55,88]  #lista

def somarNotas(*args):
  print(args)
  print(sum(args))

#somarNotas(notas)  #typeError
somarNotas(*notas) # colocar *

=========================================



"""





