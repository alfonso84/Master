import saludar
import unittest


class TestSaludar(unittest.TestCase):

    def test_saludo1(self):
        saludo = saludar()
        assert "Hola" == saludo()

    def test_saludo2(self):
        saludo = saludar()
        assert "Buenos días" == saludo()

    def test_saludo3(self):
        saludo = saludar()
        assert "Hola, ¿Qué tal?" == saludo()


if __name__ == "__main__":
    unittest.main()

