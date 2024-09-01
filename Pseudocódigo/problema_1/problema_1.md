# SISTEMA DE RESERVAS DE AEROLINEAS
## Pseudocódigo:
```
Inicio
    Leer titulo
    Leer nombre
    Leer apellido

    Escribir saludo < CONCATENAR(titulo, nombre, apellido) "¡Bienvenido a FastFast Airlines!"

    LEER origen
    LEER destino

    Si origen = destino entonces
        Escribir "El origen y el destino no pueden ser iguales."
        Terminar
    Fin si

    LEER dia_semana
    LEER dia_mes

    Si (origen = "Medellín" Y destino = "Bogotá") O (origen = "Bogotá" y destino = "Medellín") entonces
        distancia <- 240
    Si (origen = "Medellín" Y destino = "Cartagena") O (origen = "Cartagena" y destino = "Medellín") ENTONCES
        distancia <- 461
    Si (origen = "Bogotá" Y destino = "Cartagena") O (origen = "Cartagena" y destino = "Bogotá") entonces
        distancia <- 657

    Si distancia < 400 entonces
        Si dia_semana = "lunes" O "martes" O "miércoles" O "jueves" entonces
            precio <- 79900
    Sino 
        Si dia_semana = "viernes" O "sábado" O "domingo" entonces
            precio <- 119900
    Fin si

    Sino
        Si dia_semana = "lunes" O "martes" O "miércoles" O "jueves" entonces
            precio <- 156900
    Sino 
           Si dia_semana = "viernes" O "sábado" O "domingo" entonces
            precio <- 213000
    Fin si
    Fin si

    LEER preferencia_asiento

    Si preferencia_asiento = "pasillo" entonces
        letra_asiento <- "C"
    Si preferencia_asiento = "ventana" entonces
        letra_asiento <- "A"
    Si preferencia_asiento = "sin preferencia" entonces
        letra_asiento <- "B"

    numero_asiento <- numero_aleatorio(1, 29)

    asiento_final <- numero_asiento + letra_asiento

    Escribir "Tu vuelo de " + origen + " a " + destino + " del " + dia_semana + " " + dia_mes + " está reservado "
    Escribir "Precio del boleto: $ " + precio "
    Escribir "Tu asiento es: " + asiento_final
Fin
```