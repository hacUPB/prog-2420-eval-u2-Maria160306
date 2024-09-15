import os 
import random as rn
def valores_Ciclo():
    altura_Inicial = float(input("Ingrese la altura inicial del satélite (En kilómetros): "))
    while altura_Inicial <= 0:
        altura_Inicial = float(input("\n¡Error! La altura inicial no puede ser negativa o 0. \nIngrese nuevamente la altura inicial del satélite (En kilómetros): "))
    coeficiente_Arrastre = float(input("\nIngrese el valor del coeficiente de arrastre (Debe de ser un valor por debajo de 0.01): "))
    while coeficiente_Arrastre > 0.01 or coeficiente_Arrastre <= 0:
        coeficiente_Arrastre = float(input("\n¡Error! El valor del coeficiente de arrastre no puede ser negativo, cero o un valor superior a 0.01. \nIngrese nuevamente el valor del coeficiente de arrastre (Debe de ser un valor por debajo de 0.01): "))
    altura_Minima_Segura = float(input("\nIngrese la altura mínima segura del satélite (En kilómetros): "))
    while altura_Minima_Segura > altura_Inicial:
        altura_Minima_Segura = float(input("\n¡Error! El valor de la altura mínima segura no puede ser mayor a la altura inicial o menor a cero.\nIngrese nuevamente la altura mínima segura del satélite (En kilómetros): "))
    return altura_Inicial, coeficiente_Arrastre, altura_Minima_Segura

def simulacion_Orbita(altura_Inicial, coeficiente_Arrastre, altura_Minima_Segura):
    contador = 0
    altura_Actual = altura_Inicial
    while altura_Actual > altura_Minima_Segura:
        caida_Satelite = altura_Actual * coeficiente_Arrastre
        if caida_Satelite < 0.1:
            print("\nEl satélite se ha estabilizado a una altitud de:", altura_Actual,"km")
            break
        else:
            contador += 1
            altura_Actual -= caida_Satelite
            añadido_Coeficiente = round(rn.random()/1000, 6)
            coeficiente_Arrastre += añadido_Coeficiente
            print("\nÓrbita",str(contador)+": Altitud actual =", altura_Actual, "km, Coeficiente de arrastre: ", coeficiente_Arrastre)
    if caida_Satelite < 0.1:
        print("\nEl satélite ha realizado", contador, "órbitas antes de estabilizarse")
    else:
        print("\nEl satelite ha realizado", contador,"órbitas antes de reingresar a la atmósfera terrestre")

#Main
os.system('cls')
altura_Inicial, coeficiente_Arrastre, altura_Minima_Segura = valores_Ciclo()
simulacion_Orbita(altura_Inicial, coeficiente_Arrastre, altura_Minima_Segura)