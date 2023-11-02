import saludar
import unittest


class TestSaludar(unittest.TestCase):

    def test_saludo1(self):
        assert "Hola" == saludar()

    def test_saludo2(self):
        assert "Buenos días" == saludar()

    def test_saludo3(self):
        assert "Hola, ¿Qué tal?" == saludar()

    def test_saludo_con_nombre(self):
        assert "Hola, Juan" == saludar("Juan")

    def test_saludo_con_nombre_vacio(self):
        assert "Hola, Mundo!" == saludar()

    def test_saludo_con_nombre_numerico(self):
        with self.assertRaises(TypeError):
            saludar(123)


if __name__ == "__main__":
    unittest.main()
