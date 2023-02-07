#1ero definimos los subdicts por tipo de widgets:
#variableDeControl = {'indice':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'id_venta':{'tipoWidget':'controlvar', 'tipoVar':'texto'},...y así para el resto de variables de control} 

#infoEntrys = {'txtBox_indice':{'tipoWidget':'entry', 'ancho':9, 'varcontrol':'indice', 'col':2, 'fila':1, 'sticky':'NSEW'}, 'txtBox_id_venta':{'tipoWidget':'entry', 'ancho':9, 'varcontrol':'id_venta', 'col':4, 'fila':1, 'sticky':'NSEW'}}

infoLabels = {'etiqFoto':{'tipoWidget':'label', 'texto':'Foto', 'col':1, 'fila':1, 'sticky':'NSEW'}, 'etiqImagenFoto':{'tipoWidget':'label', 'texto':'', 'col':3, 'fila':1, 'sticky':'NSEW'}}

descripWidgetsCuerpoSup = {**infoLabels} #, **variableDeControl, **infoEntrys} #Y así se concatenan los diccionario de diccionarios para decrip de widgets contenidos en cuerpo superior.

#descripWidgetsCuerpoMedio = {'nombreWidget':{'tipoWidget':'hojaPorEj', 'ancho':9, 'col':0, 'fila':0, 'sticky':'NSWE'}}

#Como el cuerpo inferior generalmente se usa para los widgets de botones, su información está contenida directamente en el módulo WidgetContenedorYBotonesNav.py.

#Información para los widgets de los menús:

#Otros datos constantes:
pathCarpetaDeFotosJpg = '/home/david/Imágenes/FotosVisor/'
