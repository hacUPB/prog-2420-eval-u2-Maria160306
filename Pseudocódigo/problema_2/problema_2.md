# DESINTEGRACIÓN ORBITAL DE UN SATÉLITE
## Pseudocódigo:
```
Inicio

    Definir altitud_inicial COMO número
    Definir coeficiente_arrastre COMO número
    Definir altitud_minima_segura COMO número

    Leer altitud_inicial
    Leer coeficiente_arrastre
    Leer altitud_minima_segura

    altitud_actual <- altitud_inicial
    orbita < 0

    Imprimir "Simulando la desintegración orbital..."

    Mientras altitud_actual > altitud_minima_segura hacer

        orbita < orbita + 1

        altitud_perdida < coeficiente_arrastre * altitud_actual
        altitud_actual < altitud_actual - altitud_perdida
        coeficiente_arrastre < coeficiente_arrastre + 0.0001

        Imprimir "Órbita " + orbita + ": Altitud actual = " + altitud_actual + " km, Coeficiente de arrastre = " + coeficiente_arrastre "

        Si altitud_perdida < 0.001 entonces
            Imprimir "El satélite se ha estabilizado en una órbita baja después de " + orbita + " órbitas "
            Terminar bucle
        Fin si

    Fin mientras

    Si altitud_actual <= altitud_minima_segura entonces
        Imprimir "El satélite ha reingresado en la atmósfera terrestre después de " + orbita + " órbitas."
    Fin si
Fin
```