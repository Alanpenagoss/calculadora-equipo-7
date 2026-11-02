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
    print("Resultado:", resultado)


def main():
    while True:
        print("\nCalculadora del equipo 7")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "5":
            print("Hasta luego.")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opcion no valida.")
            continue

        a, b = obtenerNumeros()

        try:
            if opcion == "1":
                resultado = suma(a, b)
            elif opcion == "2":
                resultado = resta(a, b)
            elif opcion == "3":
                resultado = multiplicacion(a, b)
            else:
                resultado = division(a, b)

            mostrarResultados(resultado)
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
