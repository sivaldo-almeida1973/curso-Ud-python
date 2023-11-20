import unittest

from SetUp_TearDown import BolsaValores

class SetUpTearDownTestes(unittest.TestCase):

  def setUp(self):
    print('Iniciamos Teste!')
    self.pessoa = BolsaValores('Mario', 123456)

  def test_deposito_falha(self):
    self.assertEqual(self.pessoa.deposito(-100), 'Valor de deposito deve ser positivo!')


  def test_deposito_concluido(self):
    self.pessoa.deposito(100) #deposito de 100reais
    self.assertEqual(self.pessoa.saldo,100) #verificar se saldo == 100

  def test_compra_acao_concluido(self):
    self.pessoa.deposito(100)
    self.pessoa.compra_acao('Weg')
    self.assertEqual(self.pessoa.saldo,65)#testa se atualizou saldo


  def test_compra_acao_falha(self):
    self.assertEqual(self.pessoa.compra_acao('Weg'), 'Saldo Insuficiente para compra, vá ao mercado infracionario!')
    

  def tearDown(self):
    print('teste finalizado!')

    
if __name__ == '__main__':
  unittest.main()