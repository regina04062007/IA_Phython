from tkinter import *

class Menu:
    def __init__(self):
        self.window = Tk()
        self.window.title("Menu de ejercicios")
        self.window.geometry("300x430")
        self.window.config(bg="beige")
        
        Label(self.window, text="Selecciona una opcion", font=("Comic Sans MS", 12  ), bg="purple", fg="white").grid(row=1, column=3, pady=10)
        
        
        
        
        
        ejercicios = [
            ("Ejercicio 1", Ejercicio1),
            ("Ejercicio 2", Ejercicio2),
            ("Ejercicio 3", Ejercicio3),
            ("Ejercicio 4", Ejercicio4),
            ("Ejercicio 5", Ejercicio5),
            ("Ejercicio 6", Ejercicio6),
            ("Ejercicio 7", Ejercicio7),
            ("Ejercicio 8", Ejercicio8),
            ("Ejercicio 9", Ejercicio9),
            ("Ejercicio 10", Ejercicio10),
        
        ]
        
        for i, (texto, clase) in enumerate(ejercicios, start=2):
            Button(self.window, text=texto, command=lambda c=clase: c(), bg="pink").grid(row=i, column=2, pady=5)
        
        self.window.mainloop()
        
class Ejercicio1:

    def __init__(self):
        self.window=Toplevel()
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

class Ejercicio2:

    def __init__(self):
        self.window=Toplevel()
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

class Ejercicio3:

    def __init__(self):
        self.window=Toplevel()
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
            
class Ejercicio4:

    def __init__(self):
        self.window=Toplevel()
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

class Ejercicio5:
    def __init__(self):
        self.window=Toplevel()
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

class Ejercicio6:
    def __init__(self):
        self.window = Toplevel()
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

class Ejercicio7:
    def __init__(self):
        self.window=Toplevel()
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
           
class Ejercicio8:
    def __init__(self):
        self.window=Toplevel()
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

class Ejercicio9:
    def __init__(self):
        self.window=Toplevel()
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

class Ejercicio10:
    def __init__(self):
        self.window = Toplevel()
        self.window.title("Ejercicio 10")
        self.window.geometry('900x500')
        self.window.config(bg='beige')
        self.tituloLabel = Label(self.window, text="Cálculo de pago de trabajador", font=("Comic Sans MS", 12), bg="pink")
        self.tituloLabel.grid(row=0, column=1, pady=10)
        self.nombreLabel = Label(self.window, text="Nombre del trabajador:", bg="pink")
        self.nombreLabel.grid(row=1, column=0, sticky="e", pady=10)
        self.miNombre = StringVar()
        self.cuadroNombre = Entry(self.window, width=20, textvariable=self.miNombre)
        self.cuadroNombre.grid(row=1, column=1)
        self.montoNormalLabel = Label(self.window, text="Pago por hora normal:", bg="pink")
        self.montoNormalLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.miMontoNormal = StringVar()
        self.cuadroMontoNormal = Entry(self.window, width=20, textvariable=self.miMontoNormal)
        self.cuadroMontoNormal.grid(row=2, column=1)
        self.horasNormalesLabel = Label(self.window, text="Horas normales trabajadas:", bg="pink")
        self.horasNormalesLabel.grid(row=3, column=0, sticky="e", pady=10)
        self.horasNormales = StringVar()
        self.cuadroHorasNormales = Entry(self.window, width=20, textvariable=self.horasNormales)
        self.cuadroHorasNormales.grid(row=3, column=1)
        self.horasExtrasLabel = Label(self.window, text="Horas extras trabajadas:", bg="pink")
        self.horasExtrasLabel.grid(row=4, column=0, sticky="e", pady=10)
        self.horasExtras = StringVar()
        self.cuadroHorasExtras = Entry(self.window, width=20, textvariable=self.horasExtras)
        self.cuadroHorasExtras.grid(row=4, column=1)
        self.hijosLabel = Label(self.window, text="Número de hijos:", bg="pink")
        self.hijosLabel.grid(row=5, column=0, sticky="e", pady=10)
        self.numeroHijos = StringVar()
        self.cuadroHijos = Entry(self.window, textvariable=self.numeroHijos)
        self.cuadroHijos.grid(row=5, column=1)

        self.boton = Button(self.window, text="Calcular pago", command=self.calcular_pago, bg="yellow")
        self.boton.grid(row=6, column=1, pady=10)
        self.pagoLabel = Label(self.window, text="", bg="beige")
        self.pagoLabel.grid(row=7, column=1, pady=10)

        self.window.mainloop()

    def calcular_pago(self):
        try:
            nombre = self.miNombre.get()
            monto_normal = float(self.miMontoNormal.get())
            horas_normales = float(self.horasNormales.get())
            horas_extras = float(self.horasExtras.get())
            hijos = int(self.numeroHijos.get())

            monto_normal_total = monto_normal * horas_normales
            monto_extra_total = horas_extras * (monto_normal * 1.5)
            bonificacion = hijos * 0.5
            pago_total = monto_normal_total + monto_extra_total + bonificacion

            self.pagoLabel.config(
                text=f"Nombre: {nombre}\n"
                     f"Monto por horas normales: {monto_normal_total:.2f}\n"
                     f"Monto por horas extra: {monto_extra_total:.2f}\n"
                     f"Bonificación por hijos: {bonificacion:.2f}\n"
                     f"Pago total: {pago_total:.2f}",
                bg="lightgreen"
            )

        except ValueError:
            self.pagoLabel.config(text="Ingrese valores numéricos válidos.", bg="red")
        
        

app=Menu()