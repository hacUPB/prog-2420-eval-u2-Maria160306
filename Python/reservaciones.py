import random as rn
import time
import os
import datetime

def ingreso_Usuario():
    titulo = input("Bienvenido a su sistema de reserva de vuelos\n¿Es usted Sr o Sra?: ").replace(" ", "").strip().capitalize()
    while titulo != "Sra" and titulo != "Sr":
        titulo = input("\n¡Error! Debe de ingresar Sr o Sra\n\nVuelva a ingresar el título: ").replace(" ", "").strip().capitalize()
    nombre = input("\nIngrese su nombre: ").replace(" ", "").strip().capitalize()
    apellido = input("\nIngrese su apellido: ").replace(" ", "").strip().capitalize()
    if titulo == "Sra":
        print(titulo + "." + " " + nombre + " " + apellido + " ¡Bienvenida a Aerolineas Peace!")
    else:
        print(titulo + " " + nombre + " " + apellido + " ¡Bienvenido a Aerolineas Peace!")
    return titulo, nombre, apellido
def vuelo():
    global ciudades
    ciudad_Origen, ciudad_Destino = "", ""
    ciudades = ("Medellin", "Medellín" ,"Bogota", "Bogotá", "Cartagena")
    ciudad_Origen = input("\nIngrese la ciudad desde la que desea partir (Medellín, Bogotá o Cartagena): ").replace(" ", "").strip().capitalize()
    ciudad_Origen = verificar_Ciudad(ciudad_Origen, ciudad_Destino)
    ciudad_Destino = input("\nIngrese la ciudad a la que desea llegar (Medellín, Bogotá o Cartagena; Distinta a la ciudad de partida): ").replace(" ", "").strip().capitalize()
    ciudad_Destino = verificar_Ciudad(ciudad_Origen, ciudad_Destino)
    ciudad_Destino = verificar_Viaje(ciudad_Origen, ciudad_Destino)
    cambio = int(input("\n¿Desea cambiar la ciudad de destino del viaje?\n1. Sí\n2. No\nIngrese el valor de la opción: "))
    cambio = verificar_Opciones_Numericas(cambio, 1, 2)
    if cambio == 1:
        ciudad_Destino = cambiar_Ciudad_Destino(ciudad_Destino, ciudad_Origen)
    return ciudad_Origen, ciudad_Destino
    
def verificar_Ciudad(ciudad_Origen, ciudad_Destino):
    if ciudad_Origen not in ciudades:
        while ciudad_Origen not in ciudades:
            ciudad_Origen = input("\n¡Error! la ciudad ingresada es incorrecta, ingrese nuevamente la ciudad desde la que desea partir (Medellín, Bogotá o Cartagena)").replace(" ", "").strip().capitalize()
        ciudad_Origen = ordenar_Ciudad(ciudad_Origen)
        return ciudad_Origen
    elif ciudad_Origen in ciudades and ciudad_Destino == "":
        ciudad_Origen = ordenar_Ciudad(ciudad_Origen)
        return ciudad_Origen
    if ciudad_Destino not in ciudades: 
        while ciudad_Destino not in ciudades:
            ciudad_Destino = input("\n¡Error! la ciudad ingresada es incorrecta, ingrese nuevamente la ciudad a la que desea llegar (Medellín, Bogotá o Cartagena; Distinta a la ciudad de partida)").replace(" ", "").strip().capitalize()
        ciudad_Destino = ordenar_Ciudad(ciudad_Destino)
        return ciudad_Destino
    else:
        ciudad_Destino = ordenar_Ciudad(ciudad_Destino)
        return ciudad_Destino
        
def ordenar_Ciudad(texto_Ciudad):
    if texto_Ciudad == "Medellin":
        texto_Ciudad = ciudades[1]
    elif texto_Ciudad == "Bogota":
        texto_Ciudad = ciudades[3]
    return texto_Ciudad
 
def verificar_Viaje(Origen, Destino):
    while Origen == Destino:
        Destino = input("\n¡Error! La ciudad de llegada no puede ser igual a la ciudad de partida\nIngrese nuevamente la ciudad de llegada (Medellín, Bogotá o Cartagena)").replace(" ", "").strip().capitalize()
        Destino = verificar_Ciudad(Origen, Destino)
    return Destino

def cambiar_Ciudad_Destino(ciudad_Destino, ciudad_Origen):
    ciudad_Destino = input("\nIngrese la ciudad a la que desea llegar (Medellín, Bogotá o Cartagena; Distinta a la ciudad de partida)").replace(" ", "").strip().capitalize()
    ciudad_Destino = verificar_Ciudad(ciudad_Origen, ciudad_Destino)
    ciudad_Destino = verificar_Viaje(ciudad_Origen, ciudad_Destino)
    return ciudad_Destino
    
def precio_Vuelo(ciudad_Origen, ciudad_Destino):
    global dias
    dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo", "miercoles", "sabado")
    dia_Semana = input("\nIngrese el día de la semana del vuelo (Lunes, Martes,..., Domingo): ").replace(" ","").strip().lower()
    dia_Semana = verificar_Dia_Semana(dia_Semana)
    dia_Semana = ordenar_Dia_Semana(dia_Semana)
    dia_Mes = int(input("\nIngrese el día del mes que desea viajar (1-30): "))
    dia_Mes = verificar_Opciones_Numericas(dia_Mes, 1, 30)
    viaje = ciudad_Origen[0] + ciudad_Destino[0]
    precio = precio_Distancia(dia_Semana, viaje)
    return dia_Semana, dia_Mes, precio

def verificar_Dia_Semana(dia_Semana):
    while dia_Semana not in dias:
        dia_Semana = input("\n¡Error! El día ingresado es incorrecto\nIngrese nuevamente el día de la semana que desea tener el vuelo (Lunes, Martes,..., Domingo): ").replace(" ","").strip().lower()
    return dia_Semana

def ordenar_Dia_Semana(texto_Dia_Semana):
    if texto_Dia_Semana == dias[7]:
        texto_Dia_Semana = dias[2]
    elif texto_Dia_Semana == dias[8]:
        texto_Dia_Semana = dias[5]
    return texto_Dia_Semana

def verificar_Opciones_Numericas(valor_Solicitado, limite_Inferior, limite_Superior):
    while valor_Solicitado < limite_Inferior or valor_Solicitado > limite_Superior:
        print("\nEl valor que ha ingresado es inválido. Recuerde que este debe de estar entre",limite_Inferior,"y",limite_Superior,)
        valor_Solicitado = int(input("Por favor ingréselo nuevamente: "))
    return valor_Solicitado

def precio_Distancia(dia_Semana, viaje):
    distancias = {"MB": 240, "BM": 240, "MC": 461, "CM": 461, "BC": 657, "CB": 657}
    distancia = distancias[viaje]
    if distancia < 400:
        if dia_Semana not in dias[4:7]:
           precio = 79900
        else:
            precio = 119900
    else:
        if dia_Semana not in dias[4:7]:
           precio = 156900
        else:
            precio = 213000
    return precio

def asignacion_Asiento():
    preferencia = int(input("\n¿Posee alguna preferencia para su asiento?\n1. Junto al pasillo\n2. Junto a la ventana\n3. Sin preferencia alguna\nIngrese el valor de la opción: "))
    preferencia = verificar_Opciones_Numericas(preferencia, 1, 3)
    if preferencia == 1:
        sufijo_Asiento = "C"
    elif preferencia == 2:
        sufijo_Asiento = "A"
    else:
        sufijo_Asiento = "B"
    numero_Asiento = str(rn.randint(1,29))
    asiento = numero_Asiento + sufijo_Asiento
    return asiento

#Main
os.system('cls')
titulo, nombre, apellido = ingreso_Usuario()
ciudad_Origen, ciudad_Destino = vuelo()
dia_Semana, dia_Mes, precio = precio_Vuelo(ciudad_Origen, ciudad_Destino)
asiento = asignacion_Asiento()
espera = "\nReservando..."
print(espera)
time.sleep(3)
os.system('cls')
print("\n¡Felicidades",titulo,nombre,apellido + "!","su vuelo de la ciudad de",ciudad_Origen,"a la ciudad de",ciudad_Destino,"del día",dia_Semana, dia_Mes, "de septiembre ha sido reservado correctamente. \nEl precio del tiquete de este es de: $", precio, "\nEl asiento asignado es: ",asiento)

recibo = int(input("\n¿Desea ver toda la información en un recibo?\n1. Sí\n2. No\nIngrese el valor de la opción: "))
recibo = verificar_Opciones_Numericas(recibo, 1, 2)
if recibo == 1:
    print("\n--------------------------------RECIBO--------------------------------\nCiudad de despegue:",ciudad_Origen,"\nCiudad de arribo:",ciudad_Destino,"\nDía de despegue:", dia_Semana.capitalize(), dia_Mes,"de Septiembre\nPrecio tiquete: $", precio,"\nAsiento asignado:",asiento)
    print("-----------------------------------------------------------------------")
    time.sleep(2)
    print("\n¡Esperamos que vuelva a preferir Aerolíneas Peace en el futuro! \n¡Gracias por usar nuestros servicios!")
else:
    print("\n¡Esperamos que vuelva a preferir Aerolíneas Peace en el futuro! \n¡Gracias por usar nuestros servicios!")