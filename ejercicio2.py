from tkinter import *
from tkinter import ttk

class Ejercicio2:

    def __init__(self):
        self.window=Tk()
        self.window.title("Ejercicio 2")
        self.window.geometry('600x250')
        self.window.config(bg = 'purple')
        self.tituloLabel=Label(self.window, text="Parque de diversiones", font=("Comic Sans MS", 12  ), bg="pink")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        self.textoLabel=Label(self.window, text="A las personas menores de 10 años se les hace un descuento del 25'%' sobre\n el precio del juego que vale 50 soles.", font=("Arial", 10  ), bg="pink")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.edadLabel=Label(self.window, text="Edad: ", bg="pink")
        self.edadLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.miEdad=StringVar()
        self.cuadroEdad=Entry(self.window, width=20, textvariable=self.miEdad)
        self.cuadroEdad.grid(row=2, column=1, sticky="e")
        self.boton=Button(self.window, text="Calcular precio a pagar", command=self.validar, bg="pink")
        self.boton.grid(row=3, column=1, pady=10)
        self.resultadoLabel=Label(self.window, text="")
        self.resultadoLabel.grid(row=4, column=1, pady=10)

        self.window.mainloop()

    def validar(self):
        try:
            edad=int(self.miEdad.get())
            precioJuego=50
            if edad < 10:
                self.resultadoLabel.config(text="Eres menor a 10 años. ")
                descuento=precioJuego*0.25
                nuevoCosto=precioJuego-descuento
            else:
                self.resultadoLabel.config(text="Eres mayor o igual a 10 años. ")
                nuevoCosto=precioJuego

            
            self.resultadoLabel.config(text=f"Total a pagar: ${nuevoCosto: }", bg="yellow")
        except ValueError:
            self.resultadoLabel.config(text="Ingrese una edad válida", bg="orange")

app=Ejercicio2()