"""
Assertions (afirmação)

Para que serve?

-Assertions permitem encontrar bugs rapidamente.
-Ele ira testar se uma afimação é verdadeira , caso sim , roda o codigo, se não retorna um erro!!
-Pode ser usado no meio do codigo, sem perdas.
-Usado para checar tipos de parametros, classes , valores...
-São usados mais, como complementos dos Unittests.

Ex 1: sem erro!

mensagem = 'tamo junto'
assert mensagem =='tamo junto'
print(mensagem)

#Ex 1: com erro!------------------------------

mensagem = 'tamo junto'
assert mensagem =='tamojunto'
print(mensagem)

#Ex 2: com erro!------------------------------

#dara um erro , mas emite uma mensagem 
mensagem = 'tamo junto'
assert mensagem =='tamojunto', 'Mensagem invalida!!'
print(mensagem)


#Ex 3: sem erro!------------------------------

#nesse caso se o numero for inteiro mostra o numero, se não mostra a msg
numero = 10
assert type(numero) is int, 'O numero não é inteiro'
print(numero)

#Ex 3: com erro!------------------------------

#nesse caso se o numero for inteiro mostra o numero, se não mostra a msg
numero = 10.0
assert type(numero) is int, 'O numero não é inteiro'
print(numero)

#Ex 4: sem erro!------------------------------

class Teste:

  def __init__(self, nome):
    self.__nome = nome

  @property
  def nome(self):
    return self.__nome
  
maria = Teste('Maria')
assert isinstance(maria, Teste)
print(maria.nome)


#Ex 5: sem erro!------------------------------

def apagaArquivos(senha):
  senhaConfirma = '123'
  assert senha == senhaConfirma
  print('Apaguei todos os seus arquivos!!')

#intanciar
apagaArquivos('123')



#Ex 5: com erro!------------------------------

def apagaArquivos(senha):
  senhaConfirma = '123'
  assert senha == senhaConfirma
  print('Apaguei todos os seus arquivos!!')

#intanciar
apagaArquivos('1234')


"""

def apagaArquivos(senha):
  senhaConfirma = '123'
  assert senha == senhaConfirma
  print('Apaguei todos os seus arquivos!!')

#intanciar
apagaArquivos('123')


