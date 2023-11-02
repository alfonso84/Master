import random
import unittest
from mock import patch


class TestSaludar(unittest.TestCase):

    @patch('random.randint', return_value=0)
    def test_saludo1(self):
        assert saludar.saludar() == "Hola"

    @patch('random.randint', return_value=1)
    def test_saludo2(self):
        assert saludar.saludar() == "Buenos días"

    @patch('random.randint', return_value=2)
    def test_saludo3(self):
        assert saludar.saludar() == "Hola, ¿Qué tal?"


if __name__ == '__main__':
    unittest.main()
