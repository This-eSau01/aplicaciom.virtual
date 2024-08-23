def envio(direccion,telefono,verificacion,plazo=30):
    lista=[]
    lista.append(direccion)
    lista.append(telefono)
    print(lista)
    if verificacion=="si":
      print(f"gracias por su compara su pedido llegara en un plazo de {plazo} minutos")
    elif Verific=="no":
      direccion=input("ingrse de nuevo la direccion ")  
      telefono=int(input("ingrese de nuevo su numero de telefono para que se comunique con el repartidor: "))
lista=[]
plazo=30       
direc=input("ingrse la direccion: ")  
telef=int(input("ingrese su numero de telefono para que se comunique con el repartidor: "))
Verific=input("ingrese si o no segun corresponda si sus datos son correctos: ")
envio(direc,telef,Verific,plazo)
