import time


def medirTiempo(f1):
    def calcular(*args, **kwargs):
        inicio = time.time()
        total = f1(*args, **kwargs)
        print("Tiempo de carga: {}".format(time.time()-inicio))

        return total
    return calcular


@medirTiempo
def division(a, b):
    time.sleep(2)
    return a/b


print(division(47, 2))
