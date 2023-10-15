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



"""



#função com parametro padrão (default)

def medida(numero, referencia= 60):
  if numero > referencia:
    print(f'{numero} é maior que {referencia}')
  else:
    print(f"{numero} é menor que {referencia}")


medida(70)




