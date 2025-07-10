import sys 

from usuarios import registrar_usuario
from ingreso_vehiculo import ingresar_vehiculo
from retiro_vehiculo import retirar_vehiculo
from administracion import menu_administracion

# funcion de crear el menú
def mostrar_menu():
    print("\n")
    print("Bienvenido al Parqueadero PARKADEMIC")  # Nombre del parqueadero según instructivo fileciteturn2file0
    print("1. Registrar Usuario")
    print("2. Ingresar Vehículo")
    print("3. Retiro Vehículo")
    print("4. Administrador")
    print("5. Salir")

def main(): 

    while True: 
        mostrar_menu()
        opcion = input("\n ----> Ingrese la opción: ")

        if opcion =='1': 
            registrar_usuario()
        elif opcion=='2':
            ingresar_vehiculo()
        elif opcion=='3': 
            retirar_vehiculo()
        elif opcion=='4': 
            menu_administracion()
        elif opcion=='5': 
            print('saliendo del sistema'.center(30))
            break
        else: 
            print('Opción inválida, Por favor seleccione una opción del 1 al 5.')

if __name__=="__main__": 
    main()
    