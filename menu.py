num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\nSeleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División real")
print("5. División entera")
print("6. Módulo")

opcion = int(input("Digite una opción: "))

if opcion == 1:
    print("Resultado:", num1 + num2)
elif opcion == 2:
    print("Resultado:", num1 - num2)
elif opcion == 3:
    print("Resultado:", num1 * num2)
elif opcion == 4:
    print("Resultado:", num1 / num2)
elif opcion == 5:
    print("Resultado:", num1 // num2)
elif opcion == 6:
    print("Resultado:", num1 % num2)
else:
    print("Opción inválida")