from tkinter import *
from tkinter import ttk
from PaquetesVisorDeFotos.Widgets.Crear import *
from PaquetesVisorDeFotos.Widgets.DescripciónDeLosWidgets import pathCarpetaDeFotosJpg#Y otras informaciones necesarias para cuerpo medio e inferior
from PaquetesVisorDeFotos.Logica.Funciones.Posicionamiento import *
from PaquetesVisorDeFotos.Logica.Funciones.AdminFotos import FotoToolsPIL

class WidgetMarco:
    def __init__(self, argraiz):
        self.framePadre = argraiz
        self.ir_a = StringVar()
        self.posicion = -1
        self.fotos = FotoToolsPIL(pathCarpetaDeFotosJpg).obtenerFotos()
        #Note que no creamos un objeto de tipo FotoToolsPIL persistente usando un apuntador-identificador para ello. 
        #Simplemente tomamos la tupla del método .obtenerFotos.
        
        #Declaramos-creamos los atributos-objetos tipo widgets. Note que self es cada widget hijo creado dentro de su padre, self.framePadre, englobado dentro del atributo-objeto de este, self.widgetSuperior:
        self.widgetSuperior = crearWidgetsYsusVarControlEnBaseAdescrip(self, self.framePadre.cuerpo_superior)
          
        #Averiguar por qué no se tiene que especificar con ** el dict descripHojaDeDatos:
        #self.widgetHojaDeDatos = crearWidgetsYsusVarControlEnBaseAdescrip(self, self.framePadre.cuerpo_medio, descripHojaDeDatos)
       
        self.botonPrimer = ttk.Button(self.framePadre.cuerpo_inferior, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("irAprimerRegistro", self.posicion)), text="<<", width=3)
        self.botonPrimer.grid(column=0, row=1, sticky=NSEW)
        self.botonRetro = ttk.Button(self.framePadre.cuerpo_inferior, text="<", width=2, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("retroceder", self.posicion)))
        self.botonRetro.grid(column=1, row=1, sticky=NSEW)
        self.botonAvance = ttk.Button(self.framePadre.cuerpo_inferior, width=2, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("avanzar", self.posicion)), text=">")
        self.botonAvance.grid(column=2, row=1, sticky=NSEW)
        self.botonUltimo = ttk.Button(self.framePadre.cuerpo_inferior, text=">>", command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("irAultimoRegistro", self.posicion)), width=3)
        self.botonUltimo.grid(column=3, row=1, sticky=NSEW)
        self.botonIrA = ttk.Button(self.framePadre.cuerpo_inferior, text="Buscar", command=lambda:self.actualizarWidgetsEnNuevaPosicion(indiceDelElementoEnTupla(self.ir_a.get(), self.posicion)))
        self.botonIrA.grid(column=4, row=1, sticky=NSEW)
        ttk.Entry(self.framePadre.cuerpo_inferior, width=7, textvariable=self.ir_a).grid(column=5, row=1) 
        
    def actualizarWidgetsEnNuevaPosicion(self, *args): 
        self.posicion =  args[0]
        self.etiqImagenFoto['image'] = self.fotos[self.posicion]                             