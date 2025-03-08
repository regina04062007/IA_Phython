from tkinter import *
from tkinter import ttk

class Ejercicio9:
    def __init__(self):
        self.window=Tk()
        self.window.title("Ejercicio 9")
        self.window.geometry('800x300')
        self.window.config(bg = 'grey')
        self.tituloLabel=Label(self.window, text="Suma de números hasta el 100 ", font=("Comic Sans MS", 12  ), bg="pink")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        self.textoLabel=Label(self.window, text="Escriba un algoritmo que sume los números ingresados por el usuario y cuando la \n suma sea superior a 100 deje de pedir números y muestre el total.", font=("Arial", 10  ), bg="pink")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.numeroEnteroLabel=Label(self.window, text="Ingrese un numero: ", bg="pink")
        self.numeroEnteroLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.numeroEntero=StringVar()
        self.cuadroNumero=Entry(self.window, textvariable=self.numeroEntero)
        self.cuadroNumero.grid(row=2, column=1, sticky="w")
        self.boton=Button(self.window, text="Agregar", command=self.validar)
        self.boton.grid(row=3, column=1, pady=10)
        self.resultadoLabel=Label(self.window, text="")
        self.resultadoLabel.grid(row=4, column=1, pady=10)

        self.sumaTotal=0

        self.window.mainloop()

    def validar(self):
        try:
            numero=int(self.numeroEntero.get())
            self.sumaTotal+=numero
            if self.sumaTotal > 100:
                self.resultadoLabel.config(text=f"Suma total: {self.sumaTotal}", bg="orange")
                self.cuadroNumero.config(state=DISABLED)
                self.boton.config(state=DISABLED)
            else:
                self.resultadoLabel.config(text=f"Suma total: {self.sumaTotal}", bg="yellow")
        except ValueError:
                self.resultadoLabel.config(text=f"Ingrese un numero valido", bg="red")
        self.resultadoLabel.set("")

app=Ejercicio9()
