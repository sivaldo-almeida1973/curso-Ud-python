"""
Propriedades:
-Metodos publicos utilizados para manipular atributos/metodos privados.


"""
#EX:
class Celular:

  def __init__(self, data, senha, saldoBanco , msg):
    self.__data = data  #atributos privados
    self.__senha = senha
    self.__saldoBanco = saldoBanco
    self.__msg = msg

  #metodos publicos que vai acessar atributos privados ja decorados(@porperty)
  @property
  def data(self):
    return f'Data de hoje: {self.__data}'
  
  @property
  def senha(self):
    return self.__senha
  
  @property
  def saldoBanco(self):
    return self.__saldoBanco
  
  @property
  def msg(self):
    return self.__msg
  
  #E se eu quiser alterar os dados privados ?
  @msg.setter
  def msg(self, resposta):
    self.__msg = resposta
  
  #alterar senha privada
  @senha.setter
  def senha(self, resposta):
    self.__senha = resposta

  
  @property
  def mensagem(self):
    return f'data: {self.__data} , Mensagem {self.__msg}'


#----------------------------------
cel1 = Celular('18/10/2023', 'Macarrao123', 32000, 'Olá Mundo!')
cel2 = Celular('18/10/2023', 'cachorroBranco', 12000, 'Olá Brasil!')


#accessar atribut privados sem usar name Maning

print(cel1.data)
print(cel1.senha)
print(cel1.msg)

print(f'Saldo total: {cel1.saldoBanco + cel2.saldoBanco}')


#E se eu quiser alterar os dados privados ?
# EX: (@msg.setter)

print(cel2.msg)
cel2.msg = 'Olá , Brasil , que nada!!!! Alterando msg privada'
print(cel2.msg)


#alterando senha
print(cel2.senha) #senha antiga
cel2.senha = 'sivaldo333'  #alterar senha
print(cel2.senha)  #senha nova


#metodo como propriedade
print(cel1.mensagem)
print(cel2.mensagem)