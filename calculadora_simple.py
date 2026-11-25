# Calculadora Simple en Python

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    print("=== CALCULADORA ===")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    while True:
        opcion = input("\nSelecciona una operación (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
        
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if opcion == "1":
                    resultado = sumar(num1, num2)
                    print(f"{num1} + {num2} = {resultado}")
                elif opcion == "2":
                    resultado = restar(num1, num2)
                    print(f"{num1} - {num2} = {resultado}")
                elif opcion == "3":
                    resultado = multiplicar(num1, num2)
                    print(f"{num1} × {num2} = {resultado}")
                elif opcion == "4":
                    resultado = dividir(num1, num2)
                    print(f"{num1} ÷ {num2} = {resultado}")
            except ValueError:
                print("Error: Debes ingresar números válidos")
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
