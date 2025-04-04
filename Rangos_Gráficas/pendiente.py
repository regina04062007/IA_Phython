import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def recta():
    try:
        puntoX = float(valorx.get())
        puntoY = float(valory.get())
        pendiente = float(valorm.get())

        label_error.config(text="")

        x = np.linspace(puntoX - 10, puntoX + 10, 400)
        b = puntoY - pendiente * puntoX 
        y = pendiente * x + b

        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color="blue", linewidth=2, label=f'Recta: y = {pendiente}x + {b:.2f}')
        plt.scatter(puntoX, puntoY, color='red', zorder=5, label=f'Punto ({puntoX}, {puntoY})')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.title('Gráfica de la línea recta')
        plt.legend()
        plt.show()

    except ValueError:
        label_error.config(text=" Ingresa valores válidos", fg="red")

ventana = tk.Tk()
ventana.title("Gráfica Línea Recta")
ventana.geometry("320x300")
ventana.config(bg="#BBDEFB")  

tk.Label(ventana, text="Coordenada x:", bg="#90CAF9", fg="#0D47A1").pack(pady=5)
valorx = tk.Entry(ventana, bg="white", fg="black")
valorx.pack(pady=5)

tk.Label(ventana, text="Coordenada y:", bg="#90CAF9", fg="#0D47A1").pack(pady=5)
valory = tk.Entry(ventana, bg="white", fg="black")
valory.pack(pady=5)

tk.Label(ventana, text="Pendiente (m):", bg="#90CAF9").pack(pady=5)
valorm = tk.Entry(ventana, bg="white", fg="black")
valorm.pack(pady=5)

tk.Button(ventana, text="Graficar", command=recta, bg="#1976D2").pack(pady=10)

label_error = tk.Label(ventana, text="", fg="red")
label_error.pack()

ventana.mainloop()



ventana.mainloop()
