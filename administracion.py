

'''Contraseña fija de administrador'''
ADMIN_PASSWORD = "ParkademikAdmon123"

from usuarios import usuarios
from ingreso_vehiculo import obtener_ingresos
import retiro_vehiculo


def menu_administracion():
    """
    Solicita contraseña, valida acceso y muestra submenú de reportes.
    """
    print("\n== Acceso Administrador ==")
    clave = input("Ingrese contraseña de administrador: ").strip()
    if clave != ADMIN_PASSWORD:
        print("Acceso denegado. Solo usuarios autorizados pueden entrar.")
        return

    while True:
        print("\n== Menú Administrador ==")
        print("1. Total vehículos registrados")
        print("2. Total vehículos retirados")
        print("3. Total vehículos sin retirar")
        print("4. Total pago de vehículos retirados")
        print("5. Tiempo promedio de estancia por vehículo")
        print("6. Lista de usuarios")
        print("7. Vehículo con tiempo de parqueo máximo y mínimo")
        print("8. Salir Administrador")

        opcion = input("\n---> Ingrese opción: ").strip()
        if opcion == "1":
            total_registrados()
        elif opcion == "2":
            total_retirados()
        elif opcion == "3":
            total_sin_retirar()
        elif opcion == "4":
            total_pago_retirados()
        elif opcion == "5":
            tiempo_promedio()
        elif opcion == "6":
            listar_usuarios()
        elif opcion == "7":
            vehiculo_tiempo_extremos()
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Seleccione del 1 al 8.")


def total_registrados():
    print(f"Total vehículos registrados: {len(usuarios)}")


def total_sin_retirar():
    ingresos = obtener_ingresos()
    print(f"Total vehículos sin retirar: {len(ingresos)}")


def total_retirados():
    registrados = len(usuarios)
    sin_retirar = len(obtener_ingresos())
    retirados = registrados - sin_retirar
    print(f"Total vehículos retirados: {retirados}")


def total_pago_retirados():
    historial = getattr(retiro_vehiculo, 'historial_retiros', [])
    total = sum(item.get('total', 0) for item in historial)
    print(f"Total pago de vehículos retirados: {total} pesos")


def tiempo_promedio():
    historial = getattr(retiro_vehiculo, 'historial_retiros', [])
    if not historial:
        print("No hay retiros registrados para calcular promedio.")
        return
    total_min = 0
    for item in historial:
        dif = item['hora_salida'] - item['hora_ingreso']
        total_min += dif.total_seconds() / 60
    promedio = total_min / len(historial)
    horas = int(promedio // 60)
    minutos = int(promedio % 60)
    print(f"Tiempo promedio de estancia: {horas} horas y {minutos} minutos")


def listar_usuarios():
    print("Listado de usuarios registrados:")
    for doc, data in usuarios.items():
        print(f"{doc}: {data['nombre']} {data['apellido']} - Placa: {data['placa']}")


def vehiculo_tiempo_extremos():
    historial = getattr(retiro_vehiculo, 'historial_retiros', [])
    if not historial:
        print("No hay retiros registrados para determinar extremos.")
        return
    max_t = historial[0]['hora_salida'] - historial[0]['hora_ingreso']
    min_t = max_t
    max_p = min_p = historial[0]['placa']
    for item in historial:
        dif = item['hora_salida'] - item['hora_ingreso']
        if dif > max_t:
            max_t = dif
            max_p = item['placa']
        if dif < min_t:
            min_t = dif
            min_p = item['placa']
    max_h = int(max_t.total_seconds() // 3600)
    max_m = int((max_t.total_seconds() % 3600) // 60)
    min_h = int(min_t.total_seconds() // 3600)
    min_m = int((min_t.total_seconds() % 3600) // 60)
    print(f"Vehículo con tiempo máximo: {max_p} → {max_h}h {max_m}m")
    print(f"Vehículo con tiempo mínimo: {min_p} → {min_h}h {min_m}m")


            

