import saludar
import unittest


def saludo1():
    return "Hola"


def saludo2():
    return "Buenos días"


def saludo3():
    return "Hola, ¿Qué tal?"


class TestSaludar(unittest.TestCase):

    def test_saludo1(self):
        assert "Hola" == saludar1()

    def test_saludo2(self):
        assert "Buenos días" == saludar2()

    def test_saludo3(self):
        assert "Hola, ¿Qué tal?" == saludar3()


if __name__ == "__main__":
    unittest.main()
