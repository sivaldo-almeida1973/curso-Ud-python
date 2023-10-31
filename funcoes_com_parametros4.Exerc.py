"""
Nomear argumentos-----------------------------


def cidade(parte1, parte2):
  print(parte1 + ' ' + parte2)

cidade('São', "Paulo")
cidade('Paulo', "São")

cidade(parte1='São', parte2='Paulo')
cidade(parte2='Paulo', parte1='São')

#=====================================================

#Parametro padrão

#função que não exige parametros
print()
input()

#função que exige parametro

def soma(num1, num2):
  print(num1 + num2)

soma(10,18)

===================================


#função com parametro padrão (default)

def medida(numero, referencia= 60):
  if numero > referencia:
    print(f'{numero} é maior que {referencia}')
  else:
    print(f"{numero} é menor que {referencia}")


medida(70)
medida(50)
medida(100)
medida(30)
medida(200)
medida(0)


======================================

def medida(numero=76, referencia= 60):
  if numero > referencia:
    print(f'{numero} é maior que {referencia}')
  else:
    print(f"{numero} é menor que {referencia}")

medida()
medida(40,50)      #se nao passar parametros ,vai valer isso
medida(70)         #se nao passar parametros ,vai valer isso

=================================
# Comando global
nome = 'arroz'  #variavel global----------

def comida():
  global nome  #Comando global converte em varivel local
  nome = nome + " e miojo"
  print(nome)

comida()



"""




# Comando local(funcao dentro de funcao)================

def funFora(): #criar funcao
  total = 0 #criar variavel 
  def funDentro(): #criar funcao dentro
    nonlocal total #faz variavel da funcao cima valer aqui
    total = total + 1
    print(total)
  return funDentro()  #pertence a funFora, retorna e fecha

funFora()







