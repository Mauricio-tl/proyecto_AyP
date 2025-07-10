from datetime import datetime
from ingreso_vehiculo import obtener_ingresos

historial_retiros=[]

ANCHO= 60

def _imprimir_carro():
    print("\n")
    print("   ______".center(ANCHO))
    print("  /|_||_\\`.__".center(ANCHO))
    print(" (   _    _ _\\".center(ANCHO))
    print(" =`-(_)--(_)-'".center(ANCHO))

def retirar_vehiculo(): 
    print("\n ==Retiro Vehiculo")
    placa= input('Ingresar placa del vehículo: ').strip().upper()
    ingresos = obtener_ingresos()

    if placa not in ingresos: 
        print(f'ERROR: No se encontro un ingreso previo para la placa {placa}.')
        return
    registro = ingresos[placa]
    hora_ingreso= registro['hora_ingreso']
    hora_salida= datetime.now()
    
    '''cálculo del tiempo total en minutos de permanencia del carro en el parqueadero '''
    diferencia=hora_salida - hora_ingreso
    minutos_totales= diferencia.total_seconds() / 60
    horas_enteras= int(minutos_totales // 60)
    minutos_restantes= minutos_totales % 60
#cuartos de hors
    cuartos= int ((minutos_restantes +14) // 15)

    valor_hora=7000
    valor_cuarto=1500
    '''condicion de pago minimo'''
    if horas_enteras== 0 and cuartos >=1 : 
        total= valor_hora

    else: 
        total= horas_enteras * valor_hora + cuartos * valor_cuarto

    # Agregar al historial antes de eliminar el ingreso
    historial_retiros.append({
        'placa': placa,
        'hora_ingreso': hora_ingreso,
        'hora_salida': hora_salida,
        'horas_enteras': horas_enteras,
        'cuartos': cuartos,
        'total': total
    })
    ingresos.pop(placa)

# Imprimir recibo
    _imprimir_carro()
    # Título
    print("PARKADEMIC".center(ANCHO, ' '))
    # Fecha
    fecha_str = hora_salida.strftime("%Y-%m-%d %H:%M:%S")
    etiqueta = "Fecha:"
    print(f"{etiqueta}{fecha_str.rjust(ANCHO - len(etiqueta))}")
    # Separador
    print("-" * ANCHO)
    # Detalles básicos
    print(f"Placa:{placa.rjust(ANCHO - len('Placa:'))}")
    print(f"Horas completas:{str(horas_enteras).rjust(ANCHO - len('Horas completas:'))}")
    print(f"Cuartos de hora:{str(cuartos).rjust(ANCHO - len('Cuartos de hora:'))}")
    # Separador antes de cobro
    print("-" * ANCHO)
    # Tabla de cobro
    time_parqueo = f"Servicio de parqueo por {horas_enteras}h {cuartos*15}m"
    print(f"{time_parqueo}{str(total).rjust(ANCHO - len(time_parqueo))}")
    print("-" * ANCHO)
    # Mensajes finales
    print("¡Gracias por preferir nuestro servicio!".center(ANCHO))
    print("Términos y condiciones: El parqueadero no se responsabiliza por daños causados por disturbios, terremotos u otros eventos externos.".center(ANCHO))





 
        