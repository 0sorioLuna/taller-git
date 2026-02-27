while True:
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "5":
        print("Saliendo...")
        break

    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print("Resultado:", n1 + n2)
    elif opcion == "2":
        print("Resultado:", n1 - n2)
    elif opcion == "3":
        print("Resultado:", n1 * n2)
    elif opcion == "4":
        print("Resultado:", n1 / n2)
    else:
        print("Opción inválida") 