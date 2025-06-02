import tkinter as tk
from tkinter import messagebox
from math import sqrt, isinf, isnan

def calcular():
    try:
        a = float(entrada1.get())
        b = entrada2.get()
        b = float(b) if b else None
        op = operacion.get()

        if op == "Suma":
            resultado = a + b
        elif op == "Resta":
            resultado = a - b
        elif op == "Multiplicación":
            resultado = a * b
        elif op == "División":
            if b == 0:
                raise ZeroDivisionError("No puedes dividir entre cero.")
            resultado = a / b
        elif op == "Cuadrado":
            resultado = a ** 2
        elif op == "Cubo":
            resultado = a ** 3
        elif op == "Potencia":
            resultado = a ** b
        elif op == "Raíz Cuadrada":
            if a < 0:
                raise ValueError("No puedes sacar raíz de número negativo.")
            resultado = sqrt(a)
        elif op == "Porcentaje":
            resultado = (a * b) / 100
        else:
            resultado = "Operación no válida"

        if isnan(resultado) or isinf(resultado):
            raise ValueError("Resultado inválido.")

        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

# Create window
raiz = tk.Tk()
raiz.title("Super calculadora de Dani")
raiz.geometry("700x400")
raiz.iconbitmap("calculadora.ico")
raiz.configure(bg="#b2ebf2")

# Upload icon
icono = tk.PhotoImage(file="flecha.png")
raiz.icono_flecha = icono  # Para evitar que la imagen se borre

# Labels y entries aligned with grid
tk.Label(raiz, text="VALOR 1:", font=("Cascadia Code", 22), bg="#b2ebf2").grid(row=0, column=0, sticky="e", padx=10, pady=10)
entrada1 = tk.Entry(raiz, font=("Cascadia Code", 18))
entrada1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(raiz, text="VALOR 2 (si aplica):", font=("Cascadia Code", 22), bg="#b2ebf2").grid(row=1, column=0, sticky="e", padx=10, pady=10)
entrada2 = tk.Entry(raiz, font=("Cascadia Code", 18))
entrada2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(raiz, text="OPERACIÓN:", font=("Cascadia Code", 22), bg="#b2ebf2").grid(row=2, column=0, sticky="e", padx=10, pady=10)

operacion = tk.StringVar(raiz)
operacion.set("Suma")
opciones = [
    "Suma", "Resta", "Multiplicación", "División",
    "Cuadrado", "Cubo", "Potencia", "Raíz Cuadrada", "Porcentaje"
]
menu = tk.OptionMenu(raiz, operacion, *opciones)
menu.config(
    font=("Cascadia Code", 18),
    width=240,
    height=20,
    bg="#f9e79f",
    fg="black",
    activebackground="#99ccff",
    image=icono,
    compound="right"
)
menu.grid(row=2, column=1, sticky="w", padx=10, pady=10)

# Button calculate centered in two columns
boton_calcular = tk.Button(
    raiz,
    text="CALCULAR",
    font=("Cascadia Code", 22),
    command=calcular,
    width=20,
    height=2,
    bg="#a2d9ce",
    fg="black",
    activebackground="#99ccff"
)
boton_calcular.grid(row=3, column=0, columnspan=2, pady=20)

# Label result centered in two columns
resultado_label = tk.Label(
    raiz,
    text="RESULTADO: ",
    font=("Cascadia Code", 22),
    bg="#b2ebf2"
)
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

raiz.mainloop()

