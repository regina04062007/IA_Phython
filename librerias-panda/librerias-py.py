import pandas as pd
import tkinter as tk
from tkinter import ttk


pd.__version__


# df_profesores1=pd.DataFrame({

#         "nombre":["Jaime","Alma","Armando","Sergio"],

#         "apellido_paterno":["Minor","Vazquez","Alvarez","Moreno"],

#          "apellido_materno":["Gomez","Sanchez","Galvan","Soto"]

#         })


# print(df_profesores1)

# print(type(df_profesores1))


df_archivo_1=pd.read_csv("Sacramentorealestatetransactions.csv")

print(df_archivo_1)

# Imprimir los primeros 5 elementos
print(df_archivo_1.head())

# Los primeros 20 elementos
print(df_archivo_1.head(20))

# Los últimos elementos
print(df_archivo_1.tail())

# Ver los tipos de datos
print(df_archivo_1.dtypes)

# Estadísticas básicas
print(df_archivo_1.describe())

# Ubicación del elemento 100
print(df_archivo_1.loc[100])

# Mostrar la columna 'city'
print(df_archivo_1["city"])

# Filtrar por ciudad 'SACRAMENTO'
print(df_archivo_1["city"] == "SACRAMENTO")


# Consultas 
def consulta1():
    #  ciudad sacreamento, número de camas=3 y precio mayor a 100000
    city = "SACRAMENTO"
    resultado1 = df_archivo_1.query("city==@city and beds==3 and price>100000")
    
    ventana_resultado1 = tk.Toplevel()
    ventana_resultado1.title("Consulta 1")
    
    frame_resultado1 = tk.Text(ventana_resultado1, height=40, width=100)
    frame_resultado1.pack(padx=10, pady=10)
    
    frame_resultado1.insert(tk.END, resultado1)

def consulta2():
    # ordenar los datos por ciudad
    resultado2 = df_archivo_1.sort_values(by="city", ascending=True)
    
    ventana_resultado2 = tk.Toplevel()
    ventana_resultado2.title("Consulta 2")
    
    frame_resultado2 = tk.Text(ventana_resultado2, height=40, width=100)
    frame_resultado2.pack(padx=10, pady=10)
    
    frame_resultado2.insert(tk.END, resultado2)

def consulta3():
    # propiedades con más de 2 baños y precio menor a 120,000.
    resultado3 = df_archivo_1.query("baths>2 and price<120000")
    
    ventana_resultado3 = tk.Toplevel()
    ventana_resultado3.title("Consulta 3")
    
    frame_resultado3 = tk.Text(ventana_resultado3, height=40, width=100)
    frame_resultado3.pack(padx=10, pady=10)
    
    frame_resultado3.insert(tk.END, resultado3)

def consulta4():
    # ordenar las propiedades por precio en orden descendente.
    resultado4 = df_archivo_1.sort_values(by="price", ascending=False)
    
    ventana_resultado4 = tk.Toplevel()
    ventana_resultado4.title("Consulta 4")
    
    frame_resultado4 = tk.Text(ventana_resultado4, height=40, width=100)
    frame_resultado4.pack(padx=10, pady=10)
    
    frame_resultado4.insert(tk.END, resultado4)

def consulta5():
    # propiedades en la ciudad citrus heights con más de 2 camas
    resultado5 = df_archivo_1.query("city=='CITRUS HEIGHTS' and beds>2")
    
    ventana_resultado5 = tk.Toplevel()
    ventana_resultado5.title("Consulta 5")
    
    frame_resultado5 = tk.Text(ventana_resultado5, height=40, width=100)
    frame_resultado5.pack(padx=10, pady=10)
    
    frame_resultado5.insert(tk.END, resultado5)

def consulta6():
    #propiedades en la ciudad sacramento o racho cordova con un precio mayor a 90,000 y que tengan  2 camas
    resultado6 = df_archivo_1.query("city in ['SACRAMENTO', 'RANCHO CORDOVA'] and price>90000 and beds==2")
    
    ventana_resultado6 = tk.Toplevel()
    ventana_resultado6.title("Consulta 6")
    
    frame_resultado6 = tk.Text(ventana_resultado6, height=40, width=100)
    frame_resultado6.pack(padx=10, pady=10)
    
    frame_resultado6.insert(tk.END, resultado6)

def consulta7():
    # propiedades conn precio de 90000 y 100000, y ordenarlas por la cantidad de camas de menor a mayor
    resultado7 = df_archivo_1.query("price>=90000 and price<=100000").sort_values(by="beds")
    
    ventana_resultado7 = tk.Toplevel()
    ventana_resultado7.title("Consulta 7")
    
    frame_resultado7 = tk.Text(ventana_resultado7, height=40, width=100)
    frame_resultado7.pack(padx=10, pady=10)
    
    frame_resultado7.insert(tk.END, resultado7)

def consulta8():
    # propiedades de Condo y tienen un area > 900 pies, y luego ordenar por estado 
    resultado8 = df_archivo_1.query("type=='Condo' and sq__ft>900").sort_values(by="state")
    
    ventana_resultado8 = tk.Toplevel()
    ventana_resultado8.title("Consulta 8")
    
    frame_resultado8 = tk.Text(ventana_resultado8, height=40, width=100)
    frame_resultado8.pack(padx=10, pady=10)
    
    frame_resultado8.insert(tk.END, resultado8)

def consulta9():
    # propiedades de tipo residencial en la ciudad rio linda que tengan mas de 1000 pies cuadrados y precio sea mayor a 100000
    resultado9 = df_archivo_1.query("type=='Residential' and city=='RIO LINDA' and sq__ft>1000 and price>100000")
    
    ventana_resultado9 = tk.Toplevel()
    ventana_resultado9.title("Consulta 9")
    
    frame_resultado9 = tk.Text(ventana_resultado9, height=40, width=100)
    frame_resultado9.pack(padx=10, pady=10)
    
    frame_resultado9.insert(tk.END, resultado9)

def consulta10():
    # propiedades con precio de 50,000 a 150,000, ordenadas por zip
    resultado10 = df_archivo_1.query("price>=50000 and price<=150000").sort_values(by="zip")
    
    ventana_resultado10 = tk.Toplevel()
    ventana_resultado10.title("Consulta 10")
    
    frame_resultado10 = tk.Text(ventana_resultado10, height=40, width=100)
    frame_resultado10.pack(padx=10, pady=10)
    
    frame_resultado10.insert(tk.END, resultado10)


ventana = tk.Tk()
ventana.title("Consultas Complejas con Pandas")
ventana.geometry("500x800")

boton = {
    "font": ("Arial", 12, "bold"),
    "bg": "#3498db",
    "fg": "white",
    "width": 15,
    "height": 2
}

boton1 = tk.Button(ventana, text="Consulta 1", command=consulta1, **boton)
boton1.pack(pady=10)

boton2 = tk.Button(ventana, text="Consulta 2", command=consulta2, **boton)
boton2.pack(pady=10)

boton3 = tk.Button(ventana, text="Consulta 3", command=consulta3, **boton)
boton3.pack(pady=10)

boton4 = tk.Button(ventana, text="Consulta 4", command=consulta4, **boton)
boton4.pack(pady=10)

boton5 = tk.Button(ventana, text="Consulta 5", command=consulta5, **boton)
boton5.pack(pady=10)

boton6 = tk.Button(ventana, text="Consulta 6", command=consulta6, **boton)
boton6.pack(pady=10)

boton7 = tk.Button(ventana, text="Consulta 7", command=consulta7, **boton)
boton7.pack(pady=10)

boton8 = tk.Button(ventana, text="Consulta 8", command=consulta8, **boton)
boton8.pack(pady=10)

boton9 = tk.Button(ventana, text="Consulta 9", command=consulta9, **boton)
boton9.pack(pady=10)

boton10 = tk.Button(ventana, text="Consulta 10", command=consulta10, **boton)
boton10.pack(pady=10)

ventana.mainloop()