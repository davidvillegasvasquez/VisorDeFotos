"""Plantilla modelo para GUI de navegación entre registros con botones de navegación vacío."""
from PaquetesVisorDeFotos.Widgets.GeometriaBase import Geometria
from PaquetesVisorDeFotos.Widgets.WidgetContenedorYBotonesNav import WidgetMarco
from tkinter import Tk

raiz = Tk()      
WidgetMarco(Geometria(raiz)) 
raiz.mainloop()
