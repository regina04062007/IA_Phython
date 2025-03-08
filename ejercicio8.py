from tkinter import *
from tkinter import ttk

class Ejercicio8:
    def __init__(self):
        self.window=Tk()
        self.window.title("Ejercicio 8")
        self.window.geometry('700x300')
        self.window.config(bg = 'grey')
        self.tituloLabel=Label(self.window, text="Sumemos numeros :D", font=("Comic Sans MS", 12  ), bg="pink")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        self.textoLabel=Label(self.window, text="Escriba un algoritmo que sume los números ingresados por el usuario hasta que el \n usuario ingrese el número 0 (detener las preguntas ante este escenario).", font=("Arial", 10  ), bg="pink")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.numeroLabel=Label(self.window, text="Ingrese un numero: ", bg="pink")
        self.numeroLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.numeroN=StringVar()
        self.cuadroNumero=Entry(self.window, textvariable=self.numeroN)
        self.cuadroNumero.grid(row=2, column=1, sticky="w")
        self.boton=Button(self.window, text="Agregar", command=self.validar)
        self.boton.grid(row=3, column=1, pady=10)
        self.resultadoLabel=Label(self.window, text="")
        self.resultadoLabel.grid(row=4, column=1, pady=10)
        
        self.sumaTotal=0
        self.window.mainloop()
        
    def validar(self):
        try: 
            numero=float(self.numeroN.get())
            if numero==0:
                self.cuadroNumero.config(state=DISABLED)
                self.boton.config(state=DISABLED)
            else:
                self.sumaTotal += numero
            self.resultadoLabel.config(text=f"Suma total acumulada: {self.sumaTotal}", bg="yellow")
        except ValueError:
            self.resultadoLabel.config(text="Ingrese un numero valido", bg="red")

        self.numeroN.set("")
            
app=Ejercicio8()
            
        