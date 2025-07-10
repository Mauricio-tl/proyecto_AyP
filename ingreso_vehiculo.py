from datetime import datetime
from usuarios import usuarios

#hora operativa del parqueadero 

HORA_INICIO= 6
HORA_FIN=24 

ANCHO= 60

def _imprimir_carro():
    print("\n")
    print("   ______".center(ANCHO))
    print("  /|_||_\\`.__".center(ANCHO))
    print(" (   _    _ _\\".center(ANCHO))
    print(" =`-(_)--(_)-'".center(ANCHO))

ingresos={}


def ingresar_vehiculo():
    ahora= datetime.now().hour
    if ahora <HORA_INICIO or ahora >=HORA_FIN: 
        print('lo sentimos, establecieminto fuera de horario de atención (06:00-24:00)')
        return
    
    print('\n== ingresasr vehiculo ==')

    tipo=input('ingrese el tipo de vehículo: ').strip().lower()
    if tipo=='moto': 
        print('Lo sentimos, no se permiten motocicletas.')
        return
    modelo= input('ingrese el modelo del vehiculo: ').strip()

    documento= input('ingrese documento del usuario: ').strip()
    if documento not in usuarios: 
        print('ERROR: usuario no registrado.')
        return
    
    placa= usuarios[documento]['placa']
    if placa in ingresos: 
        print(f'ERROR: el vehiculo de placa {placa} ya se encuentra dentro del parqueadero.')
        return
    
    hora_ingreso= datetime.now()
    ingresos[placa]={'documento':documento,
                      'hora_ingreso':hora_ingreso,
                      'tipo': tipo,
                      'modelo': modelo}
    
        # Imprimir recibo de ingreso formateado
    _imprimir_carro()
    # Título
    print("PARKADEMIC".center(ANCHO))
    # Fecha y hora
    fecha = hora_ingreso.strftime("%Y-%m-%d %H:%M:%S")
    etiqueta = "Fecha Ingreso:"
    print(f"{etiqueta}{fecha.rjust(ANCHO - len(etiqueta))}")
    # Separador
    print("-" * ANCHO)
    # Detalles del usuario y vehículo
    nombre_completo = f"Usuario: {usuarios[documento]['nombre']} {usuarios[documento]['apellido']}"
    print(f"{nombre_completo.upper()}")
    print(f"Tipo de vehículo: {tipo.upper()}")
    print(f"Modelo: {modelo.upper()}")
    print(f"Placa: {placa.upper()}")
    # Separador
    print("-" * ANCHO)
    # Mensajes finales
    print("¡Gracias por preferir Parkademic!".center(ANCHO))
    print('T&C'.center(ANCHO))
    print("El parqueadero no se responsabiliza por daños causados".center(ANCHO))
    print("por disturbios, terremotos u otros eventos externos.".center(ANCHO))

    
def obtener_ingresos():
    return ingresos