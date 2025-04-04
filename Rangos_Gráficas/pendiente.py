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

        y = pendiente * (x - puntoX) + puntoY

        plt.figure(figsize=(6, 6))
        plt.plot(x, y, label=f'Recta: y = {pendiente}(x - {puntoX}) + {puntoY}')
        plt.scatter(puntoX, puntoY, color='red', zorder=5, label=f'Punto ({puntoX}, {puntoY})')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.title('Gráfica de la linea recta')
        plt.legend()
        plt.show()

    except ValueError:
        label_error.config(text="ingresa valores válidos", fg="red")

ventana = tk.Tk()
ventana.title("Gráfica linea recta")
ventana.geometry("300x270")
ventana.config(bg="light blue")

tk.Label(ventana, text="Coordenada x :", bg="pink").pack(pady=5)
valorx = tk.Entry(ventana)
valorx.pack(pady=5)

tk.Label(ventana, text="Coordenada y :", bg="pink").pack(pady=5)
valory = tk.Entry(ventana)
valory.pack(pady=5)

tk.Label(ventana, text="Pendiente:", bg="pink").pack(pady=5)
valorm = tk.Entry(ventana)
valorm.pack(pady=5)

tk.Button(ventana, text="Graficar", command=recta, bg="yellow").pack(pady=10)

label_error = tk.Label(ventana, text="", fg="red")
label_error.pack()

ventana.mainloop()
