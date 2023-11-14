"""
Forçando dados em decoradores-----------------

def tipoDado(*tipos):#*tipos (retorna tupla, com elementos)
  def decorando(funcao):
    def convertendoDados(*args, **kwargs):
      #como args imutavel devo criar um novo para alterar o tipo das variaveis
      alteraTipo = []
      alteraTipo.append(tipos[0](args[0]))
      alteraTipo.append(tipos[1](args[1]))
      return funcao(*alteraTipo,**kwargs)
    return convertendoDados
  return decorando



@tipoDado(complex, float)
def imprimindo(num1, num2):
  print(f'Num complexo :{num1} e float {num2}')

imprimindo('2', 3)


=============================================================

B) Wraps: O que Faz?
- Copia os metadados da função antes de ser decorada para sua versão decorada.

EX:








O que são metadados?
- São dados sobre dados EX:
Decorador, voce manipula em cima de outro dado(função decorada)

EX:
-explicando o problema
# Nós ja vimos o __name__, ele retorna o nome da função a ser usada.
#Enquanto o __doc__ retorna justamente a documentação da função.



"""
from functools import wraps


def aprovados(funcao):
    """
    Essa função retorna uma lista completa do nome dos alunos aprovados
    """
    @wraps(funcao)
    def decorador(*arg , **kwargs):# conta_alunos_aprovados
      """
      Função que decora e faz os testes de notas
      """
      print(f'{aprovados.__name__}')#retornar nome da função
      print(f'{aprovados.__doc__}')#retornar documentação de aprovados

      aprovado = [] #lista vazia ,vai armazenar alunos aprovados
      for chave, nota in kwargs.items():
        if nota >= 6:
          aprovado.append(chave)
      return funcao(*aprovado) #retorna args
    return decorador

@aprovados
def conta_alunos_aprovados(*args,**kwargs):
  """
  Apresenta a quantidade de alunos aprovados.
  
  """
  print(f'{conta_alunos_aprovados.__name__}')
  print(f'{conta_alunos_aprovados.__doc__}')
  print(len(args)) #retorna args

conta_alunos_aprovados(leticia=7, Joao=5, Maria=6,Carlos=8)

