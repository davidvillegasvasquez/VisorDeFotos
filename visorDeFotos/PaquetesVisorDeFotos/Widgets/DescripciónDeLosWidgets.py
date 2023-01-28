#1ero definimos los subdicts por tipo de widgets:
variableDeControl = {'indice':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'id_venta':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'fecha':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'rif_cliente':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'ingresado':{'tipoWidget':'controlvar', 'tipoVar':'texto'}}

infoEntrys = {'txtBox_indice':{'tipoWidget':'entry', 'ancho':9, 'varcontrol':'indice', 'col':2, 'fila':1, 'sticky':'NSEW'}, 'txtBox_id_venta':{'tipoWidget':'entry', 'ancho':9, 'varcontrol':'id_venta', 'col':4, 'fila':1, 'sticky':'NSEW'}, 'txtBox_fecha':{'tipoWidget':'entry', 'ancho':9, 'varcontrol':'fecha', 'col':2, 'fila':2, 'sticky':'NSEW'}, 'txtBox_rif_cliente':{'tipoWidget':'entry', 'ancho':9,'varcontrol':'rif_cliente', 'col':4, 'fila':2, 'sticky':'NSEW'}, 'txtBox_ingresado':{'tipoWidget':'entry', 'ancho':9,'varcontrol':'ingresado', 'col':2, 'fila':3, 'sticky':'NSEW'}}

infoLabels = {'etiqIndice':{'tipoWidget':'label', 'texto':'Indice', 'col':1, 'fila':1, 'sticky':'NSEW'}, 'etiqId_venta':{'tipoWidget':'label', 'texto':'Id Venta', 'col':3, 'fila':1, 'sticky':'NSEW'}, 'etiqFecha':{'tipoWidget':'label', 'texto':'Fecha', 'col':1, 'fila':2, 'sticky':'NSEW'}, 'etiqRifCliente':{'tipoWidget':'label', 'texto':'RifCliente', 'col':3, 'fila':2, 'sticky':'NSEW'}, 'etiqIngresado':{'tipoWidget':'label', 'texto':'Ingresado', 'col':1, 'fila':3, 'sticky':'NSEW'}}

#Origen de la información para los objetos ArchivoCSV en Botones.py:
infoParent = {'columnas' : ('id_venta', 'fecha', 'rif_cliente', 'ingresado'), 'ruta' : '/home/david/Documentos/Corre/ArchivosGenerados/BDVentas/Ventas', 'nombre': 'ventas'}

infoChild = {'columnas' : ('id_venta', 'id_articul', 'cantidad'), 'ruta' : '/home/david/Documentos/Corre/ArchivosGenerados/BDVentas/DetallesVentas', 'nombre': 'detallesVenta'}

descripWidgetsCuerpoSup = {**variableDeControl, **infoEntrys, **infoLabels}

descripHojaDeDatos = {'hojaDeDatos':{'tipoWidget':'hoja', 'ancho':9, 'col':0, 'fila':0, 'sticky':'NSWE'}}
