def obtenerNumeros():
    while True:
        try:
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            return a, b
        except ValueError:
            print("Ingresa solo numeros.")


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def mostrarResultados(resultado):
    pass


def main():
    print("Calculadora del equipo 7")
    print("Estructura inicial. Funciones pendientes.")


if __name__ == "__main__":
    main()