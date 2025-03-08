from tkinter import *
from tkinter import ttk

class Ejercicio5:
    def __init__(self):
        self.window=Tk()
        self.window.title("Ejercicio 5")
        self.window.geometry('900x200')
        self.window.config(bg = 'blue')
        self.tituloLabel=Label(self.window, text="Numero entre 0 y 20", font=("Comic Sans MS", 12  ), bg="pink")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        self.textoLabel=Label(self.window, text="Escriba un algoritmo que lea del teclado un número entero y que compruebe que se encuentre en el rango (0, 20).", font=("Arial", 10  ), bg="pink")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.numeroEnteroLabel=Label(self.window, text="Ingrese un numero entre 0 y 20: ", bg="pink")
        self.numeroEnteroLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.numeroEntero=StringVar()
        self.cuadroNumero=Entry(self.window, textvariable=self.numeroEntero)
        self.cuadroNumero.grid(row=2, column=1, sticky="w")
        self.cuadroNumero.bind("<KeyRelease>", self.validar)
        self.numeroCorrectoLabel=Label(self.window, text="")
        self.numeroCorrectoLabel.grid(row=3, column=1, pady=10)

        self.window.mainloop()

    def validar(self, event):
        try:
            numero=int(self.numeroEntero.get())
            if numero > 0 and numero < 20:
                self.numeroCorrectoLabel.config(text=f"Numero válido: {numero}", bg="yellow")
            else:
                self.numeroCorrectoLabel.config(text=f"Ingrese un numero entre 0 y 20", bg="orange")
        except ValueError:
            if self.numeroEntero.get():
                self.numeroCorrectoLabel.config(text=f"Ingrese un numero entero", bg="red")
            else:
                self.numeroCorrectoLabel.config(text="")

app=Ejercicio5()
