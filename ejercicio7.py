from tkinter import *
from tkinter import ttk

class Ejercicio7:
    def __init__(self):
        self.window=Tk()
        self.window.title("Ejercicio 7")
        self.window.geometry('900x300')
        self.tituloLabel=Label(self.window, text="Calcular la suma de los primeros n numeros ", font=("Comic Sans MS", 12  ), bg="pink")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        self.textoLabel=Label(self.window, text="Escriba un algoritmo que calcule e imprima la suma de los n primeros números\n enteros positivos. El valor de n debe leerse del teclado y ser ingresado por el usuario.", font=("Arial", 10  ), bg="pink")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.numeroEnteroLabel=Label(self.window, text="Ingrese un numero: ", bg="pink")
        self.numeroEnteroLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.numeroEntero=StringVar()
        self.cuadroNumero=Entry(self.window, textvariable=self.numeroEntero)
        self.cuadroNumero.grid(row=2, column=1, sticky="w")
        self.boton=Button(self.window, text="Calcular suma", command=self.validar)
        self.boton.grid(row=3, column=1, pady=10)
        self.resultadoLabel=Label(self.window, text="")
        self.resultadoLabel.grid(row=4, column=1, pady=10)

        self.window.mainloop()

    def validar(self):
        try:
            numero=int(self.numeroEntero.get())
            if numero<=0:
                self.resultadoLabel.config(text="Ingrese números enteros positivos", bg="orange")
                return
            suma=sum(range(1, numero+1))
            self.resultadoLabel.config(text=f"La suma de los primeros numeros {numero} números es: {suma}", bg="yellow")
            
        except ValueError:
            self.resultadoLabel.config(text="Ingresa un numero valido", bg="red")
           

app=Ejercicio7()
