from PaquetesVisorDeFotos.Widgets.DescripciónDeLosWidgets import infoParent
from tkinter import messagebox
import os

def nuevaPosicionLuegoDePulsarBoton(accion, posicionActual):
    posicion = posicionActual
    primeraPosicion = 0
    longitud = 0
    
    with os.scandir('/home/david/Imágenes/FotosVisor/') as archivo:
            for foto in archivo:
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
          