import random


def aleatorio():
    lista = []
    for numero in range(10):
        num = random.randint(1, 100)
        lista.append(num)
    return lista
