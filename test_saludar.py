import saludar
import random
import unittest
from mock import patch


class TestSaludar(unittest.TestCase):

    @patch('random.randint', return_value=0)
    def test_saludo1(self, mock_randint):
        assert saludar.saludar() == "Hola"

        mock_randint.assert_called_once_with(0)

    @patch('random.randint', return_value=1)
    def test_saludo2(self, mock_randint):
        assert saludar.saludar() == "Buenos días"

        mock_randint.assert_called_once_with(1)

    @patch('random.randint', return_value=2)
    def test_saludo3(self, mock_randint):
        assert saludar.saludar() == "Hola, ¿Qué tal?"

        mock_randint.assert_called_once_with(2)


if __name__ == '__main__':
    unittest.main()
