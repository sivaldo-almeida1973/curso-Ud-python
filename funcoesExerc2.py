"""
Criar 5 funcoes: uma para cadastro, outra para realizar o login, outra para mudar a senha, outra para realizar logout e ainda uma para definir qual opcao o usuario deseja escolher.
Utilize o loop while para sair  do sistema apenas se o usuario desejar (criar a opcao 'sair).
Atente-se as regras:
  -so é possivel realizar cadastro se não houver nenhum anterior.
  -so é possivel realizar login se houver cadastro.
  -so é possivel realizar login se o usuario informar corretam. username e senha.
  -so é possivel alterar a senha se o usuario estiver logado.
  -so é possivel alterar a senha se o usuario informar corretamente a senha atual.
  -so é possivel realiza logout se o usuario estiver logado.
  -


"""
login = False
cadastroFeito = False
op = 0
userName = ''
senha = ''

def intro():
  global op  #recebe as variaveis
  global cadastroFeito
  global login
  while op != 5:
    print('1 - Cadastro\n2 - Login\n3 - Mudar senha\n4 - Logout\n5 - Sair')
    op = int(input('----------Opção:'))

    if op ==1:
      if not cadastroFeito: #se não existir cadastro anterior
        cadastro()
        
      else:
        print('------------Cadastro já feito anteriormente-------------')
    elif op == 2:
      if cadastroFeito:
        loginSistema()
        
      else:
        print('---------Faça o cadastro antes de fazeer login:---------- ')
    elif op == 3:
      if cadastroFeito:
        mudarSenha()
        
      else:
        print('--------faça o cadastro antes de alterar a senha--------')
    elif op == 4:
      if login:
        logout()
        
      else:
        print('----------Para dar logout , primeiro faça seu login----------')
    elif op == 5:
      return 0
    


#Criar funções

def cadastro():
  global userName
  global senha
  global cadastroFeito
  userName = input('--------Digite seu nome de usuario:')
  senha = input('--------Digite sua senha')
  cadastroFeito = True
  return intro() # chama a funcao principal(intro()) novamente



def  loginSistema():
  global userName
  global senha
  global login
  if not login:
     testeUsuario = input('--------UserName: ')
     testeSenha = input('----------------Senha: ')

     if testeUsuario == userName and testeSenha == senha:#test se usuario e senha estao corretos
       login = True
  if login:
    print('------------Voce está logado!------------') 
  else:
    print('---------Uasername ou senha incorretos!---------')
  return intro() # chama a funcao principal(intro()) novamente


def  mudarSenha():
  
  global senha
  global login
  if login:
    testeSenha = input('----------Senha atual: ')
    if testeSenha == senha:
      senha = input('----------Digite sua nova senha: ')
    else:
      print('----------Senha atual incorreta-----------')
  else:
    print('----------Faça login antes----------!')

  return intro()

  


def logout():
  global login
  login = False
  print('---------Deslogado!--------')
  return intro()


intro()  #chama a funcao pela primeira vez , iniciando o sistema.---------