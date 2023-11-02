import saludar


class TestSaludar:

    def test_saludo1(self):
        assert "Hola" == saludar.saludar()

    def test_saludo2(self):
        assert "Buenos días" == saludar.saludar("Pedro")

    def test_saludo3(self):
        assert "Hola, ¿Qué tal?" == saludar.saludar("Juan")


if __name__ == "__main__":
    unittest.main()
