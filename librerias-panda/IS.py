from tkinter import *
from tkinter import ttk
import pandas as pd
import tkinter as tk
import subprocess

class InicioSesion:
    def __init__(self):
        self.window = Tk()
        self.window.title("Inicio de Sesión")
        self.window.geometry('400x350')
        self.window.configure(bg="#f0f0f0")
        
        frame = Frame(self.window, bg="white", padx=20, pady=20, bd=2)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        Label(frame, text="INICIO DE SESIÓN", font=("Arial", 16, "bold"), bg="white", fg="#333").grid(row=0, column=0, columnspan=2, pady=10)
        
        self.correoLabel=Label(frame, text="Correo Electrónico", bg="pink", font=("Arial", 12))
        self.correoLabel.grid(row=1, column=0, sticky="e", pady=10)
        self.correo = StringVar()
        self.cuadroCorreo = Entry(frame, textvariable=self.correo, font=("Arial", 12), width=25, relief=SOLID, bd=1)
        self.cuadroCorreo.grid(row=1, column=1, pady=10, padx=10)
        
        self.contraLabel=Label(frame, text="Correo Electrónico", bg="pink", font=("Arial", 12))
        self.contraLabel.grid(row=2, column=0, sticky="e", pady=10)
        self.contraseña = StringVar()
        self.cuadroContraseña = Entry(frame, textvariable=self.contraseña, show="*", font=("Arial", 12), width=25, relief=SOLID, bd=1)
        self.cuadroContraseña.grid(row=2, column=1, pady=10, padx=10)
        
        self.boton = Button(frame, text="Iniciar Sesión", command=self.validar, font=("Arial", 12), bg="#4ac1a7", fg="white", relief=RAISED, bd=2)
        self.boton.grid(row=3, column=1, pady=10)
        
        self.resultadoLabel = Label(frame, text="", font=("Arial", 12), fg="red", bg="white")
        self.resultadoLabel.grid(row=4, column=1, pady=10)
        
        self.window.mainloop()
    
    def validar(self):
        correoElectronico = self.correo.get().strip()
        contra = self.contraseña.get().strip()
        
        if correoElectronico == "regina@gmail.com" and contra == "12345":
            self.mostrarVentanaConsultas() 
        else:
            self.resultadoLabel.config(text="Correo o contraseña incorrectos", fg="red")

    def mostrarVentanaConsultas(self):
        self.window.destroy() 
        subprocess.run(["python", "librerias-py.py"])

app = InicioSesion()
