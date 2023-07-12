import unittest
from codigo.backend import area_de_Concreto


class Test(unittest.TestCase):
    def test_area_de_Concreto(self):
        h = 50
        bw = 20
        self.assertEqual(area_de_Concreto(h, bw), 1000, 'Deve ser 1000')
    
    def test_area_de_Concreto2(self):
        h = 50
        bw = 20
        self.assertEqual(area_de_Concreto(h, bw), 1000, 'Deve ser 1000')


if __name__ == '__main__':
    unittest.main()