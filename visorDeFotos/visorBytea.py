import tkinter as tk
from tkinter import ttk
from PaquetesVisorDeFotos.Logica.Funciones.AdminFotos import FotoToolsPostgreSQL
from PIL import ImageTk, Image
import io
#import base64

root = tk.Tk()

def mostraPrimeraFotoDeTuplaDeFotos():
    fotosPostgre = FotoToolsPostgreSQL().obtenerFotosDeLaBDpostgre()
    buff = io.BytesIO(bytes(fotosPostgre[0]))
    imagenBitmap= Image.frombytes(mode = '1', data = buff.getvalue(), size = (120, 120), decoder_name = 'raw')
    foto = ImageTk.BitmapImage(imagenBitmap)
    img_label = ttk.Label(root, image = foto)
    img_label.grid(ipadx=80, ipady=80)
    """Seguimos sin poder desplear la foto en la etiqueta."""
mostraPrimeraFotoDeTuplaDeFotos()
root.mainloop()