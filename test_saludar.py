import saludar


class TestSaludar:

    def test_saludo1(self):
        assert "Hola, Mundo" == saludar.saludar()

    def test_saludo2(self):
        assert "Buenos días, Pedro" == saludar.saludar("Pedro")

    def test_saludo3(self):
        assert "Hola, ¿Qué tal, Juan?" == saludar.saludar("Juan")


if __name__ == "__main__":
    unittest.main()
