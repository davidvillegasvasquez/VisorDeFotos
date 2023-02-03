from datetime import datetime
import os

def id_x(strCabezera, strCola):
    ahora = datetime.now()
    return f'{strCabezera}-{str(ahora.year)[2:]}{ahora.month}{ahora.day}{ahora.hour}{ahora.minute}{ahora.second}-{strCola}'
    
def cantidadDeFotosEn(path):
    cantidad = 0
    with os.scandir(path) as directorio: #Hay que meter ese path en un modulo o clase e importarlo.
        for foto in directorio:
            if foto.is_file()  and foto.name.endswith('.jpg'):
                cantidad += 1 
    return cantidad
