
import numpy as np
import matplotlib.pyplot as plt

#Rango de 0 a 100
datos= np.arange(0,100)

#Graficar
# b es por blue y --(rayitas)
plt.plot(datos,"g--")
plt.show()

#Ejemplo 2

datos=np.arange(0,360)
datos=np.radians(datos)
#Graficar sin o cos
datos=np.sin(datos)
plt.plot(datos,"b--")
plt.xlabel('tiempo')
plt.ylabel('posición')
plt.title('Funcion seno')
plt.show()

plt.savefig("seno.png")

#Ejemplo 3 Graficar sen y cos

def h(x):
    return np.sin(x)
g= lambda x: np.cos(x)

x=np.linspace(0,10,100)
# le da un color por defecto distinto
plt.plot(x,h(x),'r--',label='seno')
plt.plot(x,g(x),label='coseno')
plt.ylabel('posicion')
plt.title('Funcion seno')
plt.legend(loc=1)
plt.grid()

#programa que grafique la linea recta dinamica, si le doy pendiente y los datos que me lo grafique