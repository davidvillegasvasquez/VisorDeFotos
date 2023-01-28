from PaquetesGUInav.Widgets.DescripciónDeLosWidgets import infoCSV_detallesVentas, infoCSV_ventas
from PaquetesGUInav.Logica.AdminArchivosCSV import ArchivoCSV
    
def listaDeListasParaTksheetSegunPosicEnPadre(posicion):
    ''
    contenidoHijo = ArchivoCSV(**infoCSV_detallesVentas).obtenerContenido()
    id_venta_PadreEnPosicion = ArchivoCSV(**infoCSV_ventas).obtenerContenido()[posicion][1]
    
    listaDeListas = []
    
    for tupla in contenidoHijo:
        if tupla[1] == id_venta_PadreEnPosicion:
            listaDeListas.append(list(tupla[2:]))
        
    return listaDeListas #Averiguar porque no puedo usar la tupla de tuplas para el tksheet. Averiguar si hay que hacer alguna configuración en este para poder usar tupla de tuplas. Resp = porque las tuplas son inmutables, y los cambios de 
    #valores en la hoja mientras navegamos sobre ella, sólo se hacen con el método set_sheet_data(). Una tupla de tuplas para data sólo serviría para una única hoja que no cambiará su contenido durante la vida del programa, sólo para fines de mostrar, sin navegación.
       