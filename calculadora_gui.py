# Calculadora Avanzada con Interfaz Gráfica (GUI)
# Requiere tkinter (incluido en Python por defecto)

import tkinter as tk
from tkinter import messagebox

class CalculadoraGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("400x500")
        
        # Variable para almacenar la entrada
        self.pantalla = tk.Entry(ventana, font=("Arial", 20), justify="right")
        self.pantalla.grid(row=0, column=0, columnspan=4, ipady=10, padx=5, pady=5, sticky="nsew")
        
        # Botones numéricos y operadores
        botones = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "←", "√", "^"]
        ]
        
        for fila in range(len(botones)):
            for col in range(len(botones[fila])):
                boton_texto = botones[fila][col]
                boton = tk.Button(
                    ventana, text=boton_texto, font=("Arial", 18),
                    command=lambda x=boton_texto: self.al_presionar(x)
                )
                boton.grid(row=fila+1, column=col, padx=5, pady=5, sticky="nsew")
    
    def al_presionar(self, char):
        contenido = self.pantalla.get()
        
        if char == "=":
            try:
                resultado = eval(contenido)
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, str(resultado))
            except:
                messagebox.showerror("Error", "Expresión inválida")
        elif char == "C":
            self.pantalla.delete(0, tk.END)
        elif char == "←":
            self.pantalla.delete(len(contenido)-1, tk.END)
        elif char == "√":
            try:
                resultado = float(contenido) ** 0.5
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, str(resultado))
            except:
                messagebox.showerror("Error", "Número inválido")
        elif char == "^":
            self.pantalla.insert(tk.END, "**")
        else:
            self.pantalla.insert(tk.END, char)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CalculadoraGUI(ventana)
    ventana.mainloop()
