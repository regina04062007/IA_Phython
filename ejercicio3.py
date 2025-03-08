from tkinter import *
from tkinter import ttk

class Ejercicio3:

    def __init__(self):
        self.window=Tk()
        self.window.title("Ejercicio 3")
        self.window.geometry('870x300')
        self.window.config(bg = 'lightgreen')
        self.tituloLabel=Label(self.window, text="Descuento en mes de Octubre", font=("Comic Sans MS", 12  ),bg="yellow")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        self.textoLabel=Label(self.window, text="Una tienda ofrece un descuento del 15'%' sobre el total de la compra durante el mes de octubre.\n  Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar al cliente.", font=("Arial", 10  ), bg="yellow")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.mesLabel=Label(self.window, text="Mes en el que estamos (minuculas)", bg="yellow")
        self.mesLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.miMes=StringVar()
        self.cuadroMes=Entry(self.window, width=20, textvariable=self.miMes)
        self.cuadroMes.grid(row=2, column=1, sticky="e")
        self.precioTotalLabel=Label(self.window, text="Proporcione su total a pagar", bg="yellow")
        self.precioTotalLabel.grid(row=3, column=0, sticky="e", pady=10)
        self.miPrecio=StringVar()
        self.cuadroPrecioTotal=Entry(self.window, width=20, textvariable=self.miPrecio)
        self.cuadroPrecioTotal.grid(row=3, column=1, sticky="e")
        self.boton=Button(self.window, text="Calcular cantidad a cobrar", command=self.validar, bg="yellow")
        self.boton.grid(row=4, column=1, pady=10)
        self.resultadoLabel=Label(self.window, text="")
        self.resultadoLabel.grid(row=5, column=1, pady=10)

        self.window.mainloop()

    def validar(self):
        try: 
            mes = self.miMes.get().strip()
            precio=float(self.miPrecio.get())
            
            if mes=="octubre":
                descuento=precio*0.15
                nuevoPrecio=precio-descuento
                mensajeDescuento="Tienes descuento por el mes de octubre"
            else:
                nuevoPrecio=precio
                mensajeDescuento="No tienes descuento por no estar en el mes de octubre"

            self.resultadoLabel.config(text=f"{mensajeDescuento}\nTotal a pagar: ${nuevoPrecio: }", bg="lightblue")
        except ValueError:
            self.resultadoLabel.config(text="Ingrese un precio a pagar válido", bg="red")

app=Ejercicio3()
