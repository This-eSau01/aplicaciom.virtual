import re
def usuario_nombre (nombre):
    nombre = input(" Ingresar nombre ")
    return nombre

def user_apellido(apellido):
    apellido = input("Ingresar apellido")
    return apellido

def user_Dni(identificacion):
    comprobacion_dni = r'^\d{8}$'
    identificacion = input(" Numero de Docuemento ")
    if re.match(comprobacion_dni,identificacion):
        print("docuemnto de identidad valido : {} ".format(identificacion))
    else:
        print("documento de identidad icorrecto : {} ".format(identificacion))

def user_correo(correo):
    comprobacion_email = r'^[a-zA-Z0-9._%+-]+@(gmail|hotmail)\.com$'
    correo = input("Ingresar correo")
    if re.match(comprobacion_email,correo):
        print(" {} Correo valido".format(correo))
    else:
        print(" {} Coreo incorrecto".format(correo))

def user_contrasena(contrasena):
    contrasena = input("Ingresar la contrasena ")
    return contrasena