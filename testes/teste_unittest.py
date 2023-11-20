import unittest

from conhecer_Unittest import converte_padrao, par_impar

#é bom nomear as classes com o mesmo nome do módulo testado(conhecer_Unittest)
class conhecerUnittestTeste(unittest.TestCase):
#Recebe self porque a classe conhecerUnittestTeste herda de TesteCase, que por sua vez tem o metodo assertEquals,etc.
  def test_converte_padrao_tarde(self):
    """Teste para horario vespertinos e noturno"""
    self.assertEqual(converte_padrao(14, 25), '2:25 P.M', 'Deu Erro!')
  
  def test_converte_padrao_manha(self):
    """Teste para horario matutino"""
    self.assertEqual(converte_padrao(8, 10), '8:10 A.M', '')

  def test_converte_padrao_retorno(self):
    """Teste o tipo de retorna da função"""
    self.assertIs(type(converte_padrao(8,10)), str)

  def test_par_impar_par(self):
    """Teste para saber se é par"""
    self.assertTrue(par_impar(4))

  def test_par_impar_impar(self):
    """Teste para saber se é impar"""
    self.assertFalse(par_impar(5))

#essa linha é necessaria, pois podemos importar o modulo testes(reaproveitando para outros sistemas)e assim , não realizar os testes toda vez que executar o programa que o importou.
if __name__ == '__main__':
  unittest.main() #comando para criar a interface e realizar os testes em si






