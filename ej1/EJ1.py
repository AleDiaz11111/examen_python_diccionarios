import subprocess
subprocess.run("cls",shell=True)
tienda = {
    "accion": ["PLP enojado"],
    "CF": ["Aprovar el año Simulator"],
    "terror": ["La PETec de la furia","Examen Programacion"]
}

biblioteca = {}
c = 1

while True:
    print("- - - - - - - - - - - - -")
    print("|       ETec Station      |")
    print("- - - - - - - - - - - - -")
    print("1. Tienda")
    print("2. Jugar")
    print("3. Salir")
    
    op = input("> ")

    if op == "1":
        print("1. Comprar un juego")
        print("2. Ingresar un juego")
        print("3. Salir")
        sub = input("> ")

        if sub == "1":
            g = input("Genero: ")
            if g in tienda:
                n = 0
                for juego in tienda[g]:
                    print(str(n) + ". " + juego)
                    n = n + 1
                pos = int(input("Numero: "))
                biblioteca[c] = tienda[g][pos]
                c = c + 1

        elif sub == "2":
            g = input("Genero: ")
            nom = input("Titulo: ")
            if g in tienda:
                tienda[g].append(nom)
            else:
                tienda[g] = [nom]
    elif op == "2":
        for x in biblioteca:
            print(str(x) + ": " + biblioteca[x])
        if biblioteca:
            id_j = int(input("Que juego: "))
            input("Jugando a " + biblioteca[id_j] + "...")

    elif op == "3":
        break