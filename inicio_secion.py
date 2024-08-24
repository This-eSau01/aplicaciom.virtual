import re

def correo_incio_seccion(correo_electronico):
    comprobacion_email = r'^[a-zA-Z0-9._%+-]+@(gmail|hotmail)\.com$'
    correo_electronico = input("Ingresar correo")
    if re.match(comprobacion_email,correo_electronico):
        print(" {} Correo  valido :  ".format(correo_electronico))
    else:
        print(" {} Correo incorrecto : ".format(correo_electronico))

def contrasena_inicio_seccion(contrasena):
    contrasena = input("Ingresar la contrasena ")
    return contrasena
