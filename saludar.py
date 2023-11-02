import random


class Saludos:

    def __init__(self):
        self.saludos = ["Hola", "Buenos días", "Hola, ¿Qué tal?"]

    def get_saludo(self, nombre=None):
        if nombre is None:
            nombre = "Mundo"
        return f"{self.saludos[0]}, {nombre}!"


def saludar(nombre=None):
    saludos = Saludos()
    saludo = saludos.get_saludo(nombre)
    print(saludo)

