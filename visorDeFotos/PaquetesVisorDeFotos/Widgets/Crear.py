from tkinter import ttk
from tkinter import *
from tksheet import *
from PaquetesVisorDeFotos.Widgets.DescripciónDeLosWidgets import infoChild

def crearWidgetsYsusVarControlEnBaseAdescrip(widget, widgetPadre, descripWidget):
    for nombreWidget, val in descripWidget.items():
        #1ero, creamos las variables de control tkinter. Note como la función setattr, al no encontrar el objeto a setear su atributo-propiedad, lo crea, tal "with open(ruta, mode='r+') as archivo" crea el archivo al no encontrarlo:
        tipo = descripWidget[nombreWidget]['tipoWidget']
        
        if tipo == "controlvar":
            if val['tipoVar'] == 'texto': setattr(widget, nombreWidget, StringVar())
            if val['tipoVar'] == 'entero': setattr(widget, nombreWidget, IntVar())
            if val['tipoVar'] == 'decimal': setattr(widget, nombreWidget, DoubleVar())
            if val['tipoVar'] == 'boolean': setattr(widget, nombreWidget, BooleanVar())  
      
        #Y ahora vamos con los widgets. Primero los declaramos:
        if tipo == "label":
            setattr(widget, nombreWidget, ttk.Label(widgetPadre, text=val['texto']))
        
        if tipo == "entry":
            setattr(widget, nombreWidget, ttk.Entry(widgetPadre, width=val['ancho'], textvariable = widget.__dict__[val['varcontrol']]))
        
        if tipo == "hoja":
            setattr(widget, nombreWidget, Sheet(widgetPadre, column_width=70, align="center", header_align="center", height=130, width=250, headers = infoChild['columnas'][1:])) #Siempre quitaremos el campo clave entre el padre e hijo. Aquí lo hacemos desde el descriptor, de modo que no tiene indice y siempre cortamos a partir de 1 ([1:]). 
               
        #Y así sucesivamente para el resto de otros widgets (botones, frame, etc.)
        
        #Por último, dibujamos el widget. Aquí si debemos filtrar que no sea un atributo-objeto tipo variable de control tkinter para poder dibujarlo:
        if tipo != "controlvar":
            widget.__dict__[nombreWidget].grid(column=val['col'], row=val['fila'], sticky=val['sticky'])

