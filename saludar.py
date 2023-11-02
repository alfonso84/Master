import random


class Saludos:

    def __init__(self):
        self.saludos = ["Hola", "Buenos días", "Hola, ¿Qué tal?"]

    def get_saludo(self):
        return self.saludos[random.randint(0, len(self.saludos) - 1)]


def saludar(nombre=None):
    saludos = Saludos()
    saludo = saludos.get_saludo()
    if nombre is None:
        print(saludo)
    else:
        print(f"{saludo}, {nombre}")


saludar()
