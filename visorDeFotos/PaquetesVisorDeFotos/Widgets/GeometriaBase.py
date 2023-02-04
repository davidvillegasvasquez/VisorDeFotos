from tkinter import * 
from tkinter import ttk
from PaquetesVisorDeFotos.Widgets.Crear import *
from PaquetesVisorDeFotos.Widgets.DescripciónDeLosWidgets import descripWidgetsCuerpoSup

class Geometria:
    def __init__(self, argRaiz):   
        self.raizTk = argRaiz
        self.raizTk.title("VISOR DE FOTOS")
        # Cuerpo superior(lo colocamos en row = 1 para dejarnos margén de maniobra para una eventual necesidad de agregar):
        self.cuerpo_superior = ttk.Frame(self.raizTk)
        self.cuerpo_superior.grid(column=1, row=1, sticky=(N, W, E, S))
        
        self.cuerpo_medio = ttk.Frame(self.raizTk)
        self.cuerpo_medio.grid(column=1, row=2)
        
        self.cuerpo_inferior = ttk.Frame(self.raizTk)
        # En la columna 0 y fila 1 de argroot (mitad vertical).
        self.cuerpo_inferior.grid(column=1, row=3)
        
        self.barraMenú = Menu(self.raizTk)
        # Con la opción de configuración menu del widget dónde irá el menú (que la interfaz raíz), visibilizamos el menú: es remotamente equivalente al grid.
        # La propiedad menu del widget, en este caso la interfaz raíz, tendrá como valor el menú que instanciamos sobre el, y que apuntamos con el identificador barraMenú.
        self.raizTk['menu'] = self.barraMenú

        # Para aspecto moderno y no desacoplable de los menú, antes de crear cualquiera de ellos, colocamos esta proposición:
        self.raizTk.option_add('*tearOff', FALSE)
        
        # Creamos el primer menú contenido en barraMenú, apuntado por el identificador menu1:
        self.menu1 = Menu(self.barraMenú)
        # Creamos otro menú que ya veremos que le agregamos. Puede ser versión, ayuda, acerca de, etc.
        self.menu2 = Menu(self.barraMenú)
        # Agregamos los menú creado en la barra de menú barraMenú.
        self.barraMenú.add_cascade(label="POSTGRE BYTEA", menu=self.menu1)
        self.barraMenú.add_cascade(label="MENÚ 2", menu=self.menu2)
        
        # Agregamos los comandos a los menús:
        self.menu1.add_command(label="Ingresar foto", command = self.ingresarFotosByteaEnPostgre)
        self.menu1.add_command(label="Extraer fotos", command="")
        self.menu2.add_command(command="", label="Coman1 en menu2")
        self.menu2.add_command(label="Coman2 en menu2")
        
    def ingresarFotosByteaEnPostgre(self, *args):
        self.top = Toplevel(height = 200, width = 100)
        self.top.title('Ingreso de Fotos')
        ttk.Label(self.top, text='Ubicación carpeta de fotos:').grid(row=1, column=1)
        ttk.Entry(self.top, width= 20, textvariable = '').grid(row=1, column=2)
        self.top.grab_set()      
