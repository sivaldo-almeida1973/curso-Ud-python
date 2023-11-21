import unittest

from teste_setUp_tearDown_exerc import Tatu


class ExSetUpTearDownTestes(unittest.TestCase):

  def setUp(self):
    self.bola = Tatu('Bola')
    self.napoleao = Tatu('Napoleão')

  def test_comer(self):
    self.assertEqual(self.bola.comer(), 'Sou o Bola e estou comendo pizza!')


  def test_beber(self):
    self.assertEqual(self.napoleao.beber(), 'Sou o Napoleão e estou bebendo suco!')

  def test_cavar(self):
      self.assertEqual(self.napoleao.cavar(), 'Sou o Napoleão e estou cavando sua grama!')

  def test_acasalar(self):
      self.assertEqual(self.bola.acasalar(), 'Sou o Bola e quero um filhote!')

  def tearDown(self):
    print('Teste concluido!')  

if __name__ == '__main__':
   unittest.main()

