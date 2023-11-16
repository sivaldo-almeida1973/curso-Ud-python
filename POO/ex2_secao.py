"""
Crie uma classe Robo para controlar o objeto R2D2 com os seguintes métodos:
- Construtor: Recebe como atributo a bateria que varia entre 0 e 100 e cria um atributo de instancia chamado estado
que apresenta se o robô está ligado ou desligado.
----------------------------------------------------------------
- liga_desliga: Quando esse método é chamado o robô passa a ser ligado caso esteja desligado e vice-versa.
-----------------------------------------------------------------
- movimento: Recebe como atributo uma string, que representa qual o lado que o robô irá andar e decresce o
atributo bateria em 10 para cada execução desse método.
-------------------------------------------------------------------
- controle_energia: Imprime os atributos estado e bateria atualizados do Robo.
Crie uma interface de menu para o Usuário decidir o que irá fazer com o Robo, ou seja,
qual método irá acessar. Faça tratamento de erros com Try/Except/Else/Finally.
Trate também as condições especiais como bateria zerada o que irá acontecer com o seu R2D2?
Dentre outros, fica a cargo de cada programador.
"""

#- Construtor: Recebe como atributo a bateria que varia entre 0 e 100 
# criar um atributo de instancia chamado estado que apresenta se o robô está ligado ou desligado.
class Robo:

  def __init__(self, bateria):
    self.bateria = bateria
    self.estado = 'Desligado'  #atributo de instancia(desligado)

  def liga_desliga(self):  #metodo
    if self.bateria == 0:
      print('\nBateria descarregada, carregue-a!!\n')
      self.estado == 'Desligado'
    else:
      if self.estado == 'Desligado': #se estiver desligado
        self.estado = 'Ligado'       #passa para ligado
        print('\nRobo ligado!\n')
      else:   #se não
        self.estado = 'Desligado'  
        print('Robo desligado!')


  def movimento(self,lado_andar_robo ):
    if self.bateria == 0:
      print('\nBateria Zerada, carregue o R2D2!\n')
    else:
      if self.estado == 'Desligado':
        print('\nRobo desligado, ligue-o para movimentar!\n')
      else:   
        self.lado_andar_robo = lado_andar_robo
        self.bateria = self.bateria - 10  #bateria diminui -10 quando lado escolh
        if self.bateria == 0:
          self.estado = 'Desligado'
    

  def controle_energia(self):
    print(self.estado)
    print(self.bateria)


print('-----------------------MENU ----------------------------')

try:
  #corrige problema de range
  bateria = -1 #Inicializar bateria (força a entrar no loop)
  while bateria > 100 or bateria < 0: #controla o range da bateria
    bateria = int(input('Digite a bateria do Robo: '))
    R2D2 = Robo(bateria)  #criar obj
except ValueError:
  print('Opção Invalida!')
else:
  finalizar = '' #variavel de parada do while----------

  while finalizar != 'sair': #executa o bloco-----------
      
      try:
        #criar interface De Menu Para o Usuario
        opcao = int(input('Digite o numero do comando que deseja: \n'
                          
                          '1 - Liga/Desliga o Robo\n'
                          '2 - Movimentar o Robo\n'
                          '3 - Controle de energia o Robo\n'
                          '4 - Finalizar o programa\n'
                          ' Escolha: '                  
                          ))
      except ValueError:
        print('\nOpção Invalida!\n')
      else:
        if opcao == 1:
          R2D2.liga_desliga()
        elif opcao == 2:
          R2D2.movimento(input('\nDigite o lado para o qual o robo irá andar!\n'))
        elif opcao == 3:
          R2D2.controle_energia()
        elif opcao == 4:
          finalizar = 'sair'
        else:
          print('\nEscolha uma opção de 1 a 4 !\n')
finally:
  print('Programa finalizado!')
 