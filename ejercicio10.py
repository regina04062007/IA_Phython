from tkinter import *

class Ejercicio10:
    def __init__(self):
        self.window = Tk()
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

app = Ejercicio10()
