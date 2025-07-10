#crearemos un diccionario para registrar los usuarios con sus datos. 

usuarios={}

def _obtener_nombre():
    while True:
        nombre=input('Ingrese su nombre (min. 3 letras, solo letras: ').strip()
       
        if len(nombre) < 3: 
            print('ERROR. El nombre debe tener al menos 3 letras.')
            continue
        if not nombre.isalpha(): 
            print('Error. El nombre solo debe contener letras.')
            continue
        nombre=nombre.capitalize()
        return nombre

def _obtener_apellido():
    while True:
        apellido=input('Ingrese su apellido (min. 3 letras, solo letras:').strip()
        apellido.capitalize()
        if len(apellido) < 3: 
            print('ERROR. El apellido debe tener al menos 3 letras.')
            continue
        if not apellido.isalpha(): 
            print('Error. El apellido solo debe contener letras.')
            continue
        apellido=apellido.capitalize()
        return apellido
    
def _obtener_documento():
    while True:
        documento=input('Ingrese su documento (de 3 letras a 15 digitos:').strip()
        if len(documento) < 3 or len(documento) >15: 
            print('ERROR. El documento debe tener entre 3 y 15 dígitos.')
            continue

        if not documento.isdigit(): 
            print('Error. El documento solo debe contener numeros.')
            continue

        if documento in usuarios: 
            print('ERROR. Documento ya esta registrado.')
            continue
        return documento
    
def _obtener_placa(): 
    while True: 
        placa = input('ingrese la placa del vehículo (3 letras y 3 némeros)').strip().upper()

        if len(placa) != 6: 
            print('ERROR. La placa debe tener 6 dígitos.')
            continue
        letras=placa[:3]
        numeros=placa[3:]
        if not letras.isalpha() or not numeros.isdigit(): 
            print('Error: el formato de la placa es de 3 letras seguido de 3 numeros.')
            continue
        return placa
def registrar_usuario(): 
    
    print("\n REGISTRAR USUARIO ")
    nombre= _obtener_nombre()
    apellido=_obtener_apellido()
    documento=_obtener_documento()
    placa=_obtener_placa()
    usuarios[documento]={'nombre':nombre,'apellido':apellido,'placa':placa}
    print(f'Usuario {nombre} {apellido} registrado exitosamente.')
    
