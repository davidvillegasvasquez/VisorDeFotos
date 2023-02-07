from PIL import ImageTk, Image
import os
from tkinter import messagebox
import sys
from  PaquetesVisorDeFotos.moduloConfiguración import configuración
import psycopg2
import base64

class FotoToolsPIL:
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
        
class FotoToolsPostgreSQL:
    def __init__(self):
        self.fotos = ()
        self.conexión = None
        
    def ingresarFotoAPostgre(self, ubicaciónFoto, *args):
        try:
            self.conexión = psycopg2.connect(**configuración()) 
            self.fotos = ()
            dibujadoEnBin = open(ubicaciónFoto, 'rb').read()
            cursor = self.conexión.cursor()
            cursor.execute("INSERT INTO tablafotos(foto) VALUES(%s)",
                    (psycopg2.Binary(dibujadoEnBin),))
            # Commit the changes to the database
            self.conexión.commit()
            self.conexión.close()
        except (Exception, psycopg2.DatabaseError) as error:
    # Note como se le agrega texto al mensage del messagebox.
            messagebox.showerror(message=str(error), title='Error')
            #sys.exit(1)
        #finally:
            #pass    
        """Ojo: no me quería agarrar el password del usuario por defecto, postgres (password authentication failed for user "postgres"). Se solucionó con los comandos en psql: 1. sudo su postgres, 2. psql, 3. \password, y 4. te pedirá ingresar tu contraseña de postgres dos veces.
        """
    def obtenerFotosDeLaBDpostgre(self, *args):
        pass                       
                                              
            