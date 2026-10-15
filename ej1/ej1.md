# Resolver el ejercicio en un archivo ej1.py en esta misma carpeta

## Consigna:

¡Acaba de salir la nueva ETec Station, consola de última generación! 

Esta consola de videojuegos va a tener precargados una serie de al menos 4 juegos inventados por vos. Cada juego va a tener su propio ID específico, y va a funcionar mostrando un menú como el siguiente: 

```
- - - - - - - - - - - - - -
|       ETec Station      |
|                         |
- - - - - - - - - - - - - -

1. Tienda
2. Jugar a un juego
3. Salir

```
El sistema debe tener un diccionario que se llame "Tienda", donde estén los juegos que hayas inventado agrupados por género, y otro que se llame "Biblioteca" donde estén los juegos en posesión del jugador con un id que va aumentando a medida se van comprando juegos.

Ejemplo:
```
tienda = {
    "acción": ["Mono enojado I", "Mono enojado II: La venganza"],
    "ciencia ficción": ["RoboBob"],
    "terror": ["La maldición de la escuela técnica"]
}

biblioteca = {
    # Vacío al principio
}
```
Si el usuario decide comprar "Mono Enojado I" primero y luego "RoboBob", la tienda quedará igual, pero en la biblioteca se mostrarán los juegos comprados de la siguiente forma:
```
tienda = {
    "acción": ["Mono enojado I", "Mono enojado II: La venganza"],
    "ciencia ficción": ["RoboBob"],
    "terror": ["La maldición de la escuela técnica"]
}

biblioteca = {
    1: "Mono Enojado I",
    2: "RoboBob"
}
```

Lo primero que verá el usuario será el menú principal con esas tres opciones. 

Dentro de la opción 1: Tienda

Otro menú con las opciones:
1. Compar un juego
    Esta opción permite ingresar un género. Al hacerlo, le muestra la lista numerada de títulos del género. Si el usuario escribió "acción" en el ejemplo aparecerá: 
    ```
    0. Mono Enojado I
    1. Mono Enojado II
    ```
    El usuario puede ingresar un número y ese juego pasará a estar en su diccionario de "biblioteca".
2. Ingresar un juego
    Se pide el género del juego a ingresar. Luego se pide el nombre del título. El valor del título será apendado a la lista que corresponda al género elegido.
3. Salir
    Vuelve al menú principal.


Dentro de la opción 2: Jugar a un juego

. Se mostrará el diccionario "biblioteca" con los juegos numerados.
. El jugador podrá ingresar un número que corresponda al título.
. Una vez elegido el juego, aparecerá permanentemente un cartel de "Jugando a [título]..." hasta que el usuario presione alguna tecla.
