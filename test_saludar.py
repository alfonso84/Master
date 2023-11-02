import saludar
import coverage

class TestSaludar:

    def test_saludo1(self):
        with coverage.start():
            assert "Hola" == saludar.saludo1()

        with coverage.stop():
            pass

    def test_saludo2(self):
        with coverage.start():
            assert "Buenos días" == saludar.saludo2()

        with coverage.stop():
            pass

    def test_saludo3(self):
        with coverage.start():
            assert "Hola, ¿Qué tal?" == saludar.saludo3()

        with coverage.stop():
            pass
