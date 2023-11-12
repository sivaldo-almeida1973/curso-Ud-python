
"""
Crie uma função que contenha 3 funções dentro:
- Uma delas deixa a string toda maiúscula.
- Outra que Soma dois números passados pelo usuário.
- E, a ultima soma um numero passado pelo usuário com um numero aleatório entre 0 e 15 com o comando randint().
A função mais externa recebe todos os parâmetros com *args e deve-se fazer tratamento com try, except caso o
usuário passe de forma errada os dados desejados. A função em args deve receber primeiro o nome da função interna
que deseja acessar e os parâmetros necessários nessa ordem especificamente. Ex: função_externa('soma_num',2,3),
no caso está chamando a função interna que soma dois números (2,3). Cada função deve imprimir seu resultado.
"""



from random import randint


#Crie uma função que contenha 3 funções dentro:

def funcaoExterna(*args):
  if args[0] == 'upper_str':
    def upper_str():
      try:     #tratar erro caso não seja string
       print(args[1].upper())
      except AttributeError:
        print('Não tem como aplicar upper() em uma variavel que não seja str!')
    return upper_str
  elif args[0] == 'soma':
    def soma():
      try:  #tratar erro caso nao seja um numero
       print(f'Soma: {args[1] + args[2]}')
      except TypeError:
        print('Deve conter apenas numeros')
      except IndexError:
        print('Deve passar dois numeros como parametro')
    return soma
  elif args[0] == 'soma_maluca':
    def soma_maluca():
      try:
       print(f'{args[1] + randint(0, 15)}')
      except TypeError:
        print('Deve conter apenas numeros!')
    return soma_maluca
  else:
    def erro(): # tratar erro caso a função passada não exista
      print('Nenhuma função chamada!')
    return erro

  




resposta = funcaoExterna('soma_maluca', 'nao')
resposta()


#verificar se funcaoExterna funciona com funcao soma()
resposta = funcaoExterna('soma', 1, 3)
resposta()

#verificar se funcaoExterna funciona funcao upper_str()
resposta = funcaoExterna('upper_str', 'teste')
resposta()

resposta = funcaoExterna('oi', 'teste')
resposta()