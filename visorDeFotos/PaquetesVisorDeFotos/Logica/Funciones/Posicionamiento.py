from tkinter import messagebox
from PaquetesVisorDeFotos.Logica.Funciones.AdminFotos import FotoTools
import os

def nuevaPosicionLuegoDePulsarBoton(accion, posicionActual):
    posicion = posicionActual
    primeraPosicion = 0
    longitud = 0
    with os.scandir('/home/david/Imágenes/FotosVisor/') as directorio: #Hay que meter ese path en un modulo o clase e importarlo.
            for foto in directorio:
                if foto.is_file()  and foto.name.endswith('.jpg'):
                    longitud += 1
   
    if accion == "irAprimerRegistro": posicion = primeraPosicion
    
    if accion == "retroceder":
    # Condición validadora de que no estamos en la primera posición (posición=1).
        if posicion > primeraPosicion:
            posicion -= 1
        else:
            pass
            
    if accion == "avanzar":
        if posicion < longitud - 1:
                posicion += 1
        else:
            pass

    if accion == "irAultimoRegistro": posicion = longitud - 1
    
    return posicion
   
def indiceDelElementoEnTupla(elementoBuscado, posicionActual):
    return 2
          