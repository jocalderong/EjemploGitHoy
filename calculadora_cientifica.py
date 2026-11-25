# Calculadora Científica (Console)

import math

class CalculadoraCientifica:
    def __init__(self):
        self.historial = []
    
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b
    
    def potencia(self, base, exponente):
        return base ** exponente
    
    def raiz_cuadrada(self, numero):
        if numero < 0:
            return "Error: Raíz de número negativo"
        return math.sqrt(numero)
    
    def porcentaje(self, numero, porcentaje):
        return (numero * porcentaje) / 100
    
    def seno(self, angulo):
        return math.sin(math.radians(angulo))
    
    def coseno(self, angulo):
        return math.cos(math.radians(angulo))
    
    def tangente(self, angulo):
        return math.tan(math.radians(angulo))
    
    def logaritmo(self, numero, base=10):
        if numero <= 0:
            return "Error: Logaritmo de número no positivo"
        return math.log(numero, base)
    
    def mostrar_menu(self):
        print("\n" + "="*40)
        print("    CALCULADORA CIENTÍFICA")
        print("="*40)
        print("1.  Suma                    11. Seno")
        print("2.  Resta                   12. Coseno")
        print("3.  Multiplicación          13. Tangente")
        print("4.  División                14. Logaritmo")
        print("5.  Potencia                15. Historial")
        print("6.  Raíz Cuadrada           16. Limpiar Historial")
        print("7.  Porcentaje              17. Salir")
        print("="*40)
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una operación: ").strip()
            
            if opcion == "17":
                print("¡Gracias por usar la calculadora!")
                break
            
            if opcion == "15":
                if self.historial:
                    print("\n--- HISTORIAL ---")
                    for i, operacion in enumerate(self.historial, 1):
                        print(f"{i}. {operacion}")
                else:
                    print("El historial está vacío")
                continue
            
            if opcion == "16":
                self.historial.clear()
                print("Historial limpiado")
                continue
            
            try:
                if opcion in ["1", "2", "3", "4", "5", "7"]:
                    num1 = float(input("Ingresa el primer número: "))
                    num2 = float(input("Ingresa el segundo número: "))
                    
                    if opcion == "1":
                        resultado = self.sumar(num1, num2)
                        operacion = f"{num1} + {num2} = {resultado}"
                    elif opcion == "2":
                        resultado = self.restar(num1, num2)
                        operacion = f"{num1} - {num2} = {resultado}"
                    elif opcion == "3":
                        resultado = self.multiplicar(num1, num2)
                        operacion = f"{num1} × {num2} = {resultado}"
                    elif opcion == "4":
                        resultado = self.dividir(num1, num2)
                        operacion = f"{num1} ÷ {num2} = {resultado}"
                    elif opcion == "5":
                        resultado = self.potencia(num1, num2)
                        operacion = f"{num1} ^ {num2} = {resultado}"
                    elif opcion == "7":
                        resultado = self.porcentaje(num1, num2)
                        operacion = f"{num2}% de {num1} = {resultado}"
                    
                    print(f"\nResultado: {resultado}\n")
                    self.historial.append(operacion)
                
                elif opcion in ["6", "8", "9", "10", "11", "12", "13", "14"]:
                    numero = float(input("Ingresa el número: "))
                    
                    if opcion == "6":
                        resultado = self.raiz_cuadrada(numero)
                        operacion = f"√{numero} = {resultado}"
                    elif opcion == "11":
                        resultado = self.seno(numero)
                        operacion = f"sen({numero}°) = {resultado}"
                    elif opcion == "12":
                        resultado = self.coseno(numero)
                        operacion = f"cos({numero}°) = {resultado}"
                    elif opcion == "13":
                        resultado = self.tangente(numero)
                        operacion = f"tan({numero}°) = {resultado}"
                    elif opcion == "14":
                        resultado = self.logaritmo(numero)
                        operacion = f"log({numero}) = {resultado}"
                    
                    print(f"\nResultado: {resultado}\n")
                    self.historial.append(operacion)
                else:
                    print("Opción inválida")
            
            except ValueError:
                print("Error: Debes ingresar números válidos")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    calculadora = CalculadoraCientifica()
    calculadora.ejecutar()
