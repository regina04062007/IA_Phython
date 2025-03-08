from tkinter import *
from tkinter import ttk

class Ejercicio1:

    def __init__(self):
        self.window=Tk()
        self.window.title("Ejercicio 1")
        self.window.geometry('630x280')
        self.window.config(bg = 'pink')
        self.miLabel=Label(self.window, text="Aumento por trabajador", font=("Comic Sans MS", 12  ), bg="purple")
        self.miLabel.grid(row=0, column=1, pady=10)
        self.textoLabel=Label(self.window, text="Evalúe el aumento que recibe un trabajador, sabiendo que se le aplica un aumento \n del 15'%' de su sueldo básico, si este es menor de $4000 y 8'%' en caso contrario", font=("Arial", 10  ), bg="purple")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.nombreLabel=Label(self.window, text="Nombre: " , bg="purple")
        self.nombreLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.miNombre=StringVar()
        self.cuadroTexto=Entry(self.window, width=20, textvariable=self.miNombre)
        self.cuadroTexto.grid(row=2, column=1)
        self.sueldoLabel=Label(self.window, text="Sueldo: $", bg="purple")
        self.sueldoLabel.grid(row=3, column=0, sticky="e")
        self.miSueldo=StringVar()
        self.cuadroSueldo=Entry(self.window, width=20, textvariable=self.miSueldo)
        self.cuadroSueldo.grid(row=3, column=1)
        self.boton=Button(self.window, text="Calcular aumento", command=self.validar, bg="yellow")
        self.boton.grid(row=4, column=1, pady=10)
        self.resultadoLabel=Label(self.window, text="")
        self.resultadoLabel.grid(row=5, column=1, pady=10)

        self.window.mainloop()

    def validar(self):
        try:
            sueldo=float(self.miSueldo.get())
            if sueldo<4000:
                aumento=sueldo*0.15
            else:
                aumento=sueldo*0.08

            nuevoSueldo=sueldo+aumento
            self.resultadoLabel.config(text=f"Nuevo sueldo: ${nuevoSueldo}", bg="yellow")
        except ValueError:
            self.resultadoLabel.config(text="Ingrese un sueldo valido", bg="orange")

app=Ejercicio1()
        
        
