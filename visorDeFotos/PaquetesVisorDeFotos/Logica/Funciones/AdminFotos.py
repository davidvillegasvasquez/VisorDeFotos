from PIL import ImageTk, Image
import os
from tkinter import messagebox
import sys

class FotoTools:
    def __init__(self, rutaArg):
        if os.path.exists(rutaArg): 
            self.ruta = rutaArg
            self.fotos = ()
        else:
            messagebox.showerror(message="Fotos no encontradas, verifique path a carpeta de fotos", title='Error')
            sys.exit(1)
   
    def obtenerFotos(self, *args): 
        with os.scandir(self.ruta) as directorio:
            for foto in directorio:
                if foto.is_file()  and foto.name.endswith('.jpg'):
                    self.fotos += (ImageTk.PhotoImage(Image.open(os.path.join(self.ruta, foto.name))), )
        return self.fotos
                                              
            