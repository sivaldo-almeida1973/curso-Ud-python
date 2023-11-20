import unittest

from teste_unittest_exerc import acordar_cedo, tempo_exercicio, tem_exercicio

#implementar classe
class ExUnittestsTeste(unittest.TestCase):

  def test_acordar_cedo_tipo(self):
    self.assertIs(type(acordar_cedo(10)), str,'Não é string')

  def test_acordar_cedo_falha(self):
    self.assertEqual(acordar_cedo(10), 'Tente novamente amanhã!')

  def test_acordar_cedo_concluido(self):
    self.assertEqual(acordar_cedo(5), 'Você é um guerreiro!')


  def test_tempo_exercicio_concluido(self):
    self.assertEqual(tempo_exercicio(67, 3),66 )


  def test_tempo_exercicio_falha(self):
    self.assertIsNone(tempo_exercicio(67,1))

  def test_tem_exercicio_negativo(self):
    self.assertFalse(tem_exercicio('Descanso'))

  def test_tem_exercicio_afirmativo(self):
    self.assertTrue(tem_exercicio('Natação'))



if __name__ == '__main__':
  unittest.main()

