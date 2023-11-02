import random


class Saludos:

    def __init__(self):
        self.saludos = ["Hola", "Buenos días", "Hola, ¿Qué tal?"]

    def get_saludo():
        return self.saludos[0]


def saludar(nombre=None):
    saludos = Saludos()
    saludo = saludos.get_saludo()
    if nombre is None:
        nombre = "Mundo"
    print(f"{saludo}, {nombre}")

