from tkinter import *

class Ejercicio6:
    def __init__(self):
        self.window = Tk()
        self.window.title("Ejercicio 6")
        self.window.geometry('800x350')
        self.window.config(bg='lightblue')
        
        self.tituloLabel = Label(self.window, text="Numero ", font=("Comic Sans MS", 12), bg="pink")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        
        self.textoLabel = Label(self.window, text="Modifique el algoritmo del problema anterior para que cuente las veces que ha leído\n un número de teclado y escriba el resultado por pantalla.", font=("Arial", 10), bg="pink")
        self.textoLabel.grid(row=1, column=1, pady=10)
        self.textoLabel = Label(self.window, text="De Enter depues de agregar un número.", font=("Arial", 10), bg="pink")
        self.textoLabel.grid(row=2, column=1, pady=10)
        
        self.numeroEnteroLabel = Label(self.window, text="Ingrese un numero: ", bg="pink")
        self.numeroEnteroLabel.grid(row=3, column=0, sticky="e", pady=10)
        
        self.numeroEntero = StringVar()
        self.cuadroNumero = Entry(self.window, textvariable=self.numeroEntero)
        self.cuadroNumero.grid(row=3, column=1, sticky="w")
        self.cuadroNumero.bind("<Return>", self.validar)
        
        self.contadorLabel = Label(self.window, text="Cantidad de intentos: 0", font=("Arial", 10), bg="lightgray")
        self.contadorLabel.grid(row=4, column=1, pady=10)
        
        self.contador = 0
        
        self.window.mainloop()

    def validar(self, event):
        try:
            int(self.numeroEntero.get())  
            self.contador += 1  
        except ValueError:
            pass  
        
        self.contadorLabel.config(text=f"Cantidad de intentos: {self.contador}")
        self.numeroEntero.set("") 

app = Ejercicio6()
