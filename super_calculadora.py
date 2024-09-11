def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

while True:
    print("Menú:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = input("Elige una opción           (1/2/3): ")

    if opcion == '3':
        print("¡Adiós!")
        break

    if opcion in ['1', '2']:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {restar(num1, num2)}")
    else:
        print("Opción no válida, intenta de nuevo.")