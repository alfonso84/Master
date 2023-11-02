import saludar
import unittest


class TestSaludar(unittest.TestCase):

    def test_saludo1(self):
        assert "Hola" == saludar.saludo1()

    def test_saludo2(self):
        assert "Buenos días" == saludar.saludo2()

    def test_saludo3(self):
        assert "Hola, ¿Qué tal?" == saludar.saludo3()

    def test_saludo_con_nombre(self):
        assert "Hola, Juan" == saludar.saludar("Juan")

    def test_saludo_con_nombre_vacio(self):
        with self.assertRaises(ValueError):
            saludar.saludar("")

    def test_saludo_con_nombre_numerico(self):
        with self.assertRaises(TypeError):
            saludar.saludar(123)


if __name__ == "__main__":
    unittest.main()
