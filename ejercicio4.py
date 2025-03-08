from tkinter import *
from tkinter import ttk

class Ejercicio4:

    def __init__(self):
        self.window=Tk()
        self.window.title("Ejercicio 4")
        self.window.geometry('900x200')
        self.window.config(bg = 'beige')
        self.tituloLabel=Label(self.window, text="Número menor a 10", font=("Comic Sans MS", 12  ), bg="yellow")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        self.textoLabel=Label(self.window, text="Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es menor que 10.", font=("Arial", 10  ), bg="yellow")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.numeroEnteroLabel=Label(self.window, text="Ingrese un número entero menor a 10: ", bg="yellow")
        self.numeroEnteroLabel.grid(row=2, column=0,sticky="e", pady=10 )
        self.numeroEntero=StringVar()
        self.cuadroNumero=Entry(self.window,width=20, textvariable=self.numeroEntero)
        self.cuadroNumero.grid(row=2, column=1,sticky="w")
        self.cuadroNumero.bind("<KeyRelease>", self.validar)
        self.numeroCorrectoLabel=Label(self.window, text="")
        self.numeroCorrectoLabel.grid(row=3, column=1, pady=10)

        self.window.mainloop()

    def validar(self, event):
        try:
            numero=int(self.numeroEntero.get())
            if numero<10:
                self.numeroCorrectoLabel.config(text=f"Numero valido: {numero}", bg="yellow")
            else:
                self.numeroCorrectoLabel.config(text=f"Ingrese un numero menor a 10", bg="orange")
        except ValueError:
            if self.numeroEntero.get():
                self.numeroCorrectoLabel.config(text="Ingrese un numero entero", bg="red")
            else:
                self.numeroCorrectoLabel.config(text="")


app=Ejercicio4()


            


