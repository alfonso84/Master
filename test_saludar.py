import saludar


class TestSaludar:

    def test_saludo1(self):
        assert saludar.saludar() in ["Hola", "Buenos días", "Hola, ¿Qué tal?"]

    def test_saludo2(self):
        assert saludar.saludar("Pedro") in ["Hola, Pedro", "Buenos días, Pedro", "Hola, ¿Qué tal?, Pedro"]

    def test_saludo3(self):
        assert saludar.saludar("Juan") in ["Hola, Juan", "Buenos días, Juan", "Hola, ¿Qué tal?, Juan"]


if __name__ == "__main__":
    unittest.main()
