import random

def ImprimirTablero(tablero,tamaño,reinas,i):
    Marca = 0
    for fila in tablero:
        for columna in fila:
            print("\t",columna, end="")
        print("")
    n=0 
    for fila in tablero:
        for columna in fila:
            if columna == ".":
                n = 1

    if Marca == 1:
        print("Se agregaron las reinas que faltaban")
    else:
        if n==1:
            D = input("No se lleno el tablero con las reinas que diste, Te gustaria rellenar el tablero completo? Si / No:  ").title()
            if D == "Si":
                Marca = 1
                for fila in tablero:
                    for columna in fila:
                        if columna == ".":
                            GeneraReinas(1,tamaño,tablero,Marca)
                print("Tu tablero quedo llenado")
                for fila in tablero:
                    for columna in fila:
                        print("\t",columna, end="")
                    print("")
            else:
                print("Ok tu tablero queda sin rellenar")
        else:
            if i == reinas:
                print("Se ingreso las reinas necesarias para completar el tablero")
            else:
                print(f"De las {reinas} reinas que ingresaste se utilizaron {i} reinas y se eliminaron {reinas - i} reinas")

def RevisionHorizonal(tamaño,tablero,randomHorizontal,randomVertical):
    if randomVertical-1 >= 0:
        Vertical = randomVertical-1
        if tablero[randomHorizontal][Vertical] == "*" and Vertical > 0:
            while tablero[randomHorizontal][Vertical] == "*"  and Vertical > 0:
                Vertical -= 1
        while tablero[randomHorizontal][Vertical] == ".":
            tablero[randomHorizontal].pop(Vertical)
            tablero[randomHorizontal].insert(Vertical,"*")
            if Vertical > 0:
                Vertical-=1
            if tablero[randomHorizontal][Vertical] == "*":
                while tablero[randomHorizontal][Vertical] == "*" and Vertical > 0:
                        Vertical -=1

    if randomVertical+1 <= tamaño:
        Vertical = randomVertical+1
        if tablero[randomHorizontal][Vertical] == "*" and Vertical<tamaño:
            while tablero[randomHorizontal][Vertical] == "*" and Vertical<tamaño:
                Vertical +=1
        while tablero[randomHorizontal][Vertical] == ".":
            tablero[randomHorizontal].pop(Vertical)
            tablero[randomHorizontal].insert(Vertical,"*")
            if Vertical < tamaño:
                Vertical+=1
            if tablero[randomHorizontal][Vertical] == "*":
                    while tablero[randomHorizontal][Vertical] == "*" and Vertical < tamaño:
                        Vertical +=1
    RevisionVertical(tamaño,tablero,randomHorizontal,randomVertical)


def RevisionVertical(tamaño,tablero,randomHorizontal,randomVertical):
    if randomHorizontal+1 <= tamaño:
        Horizontal = randomHorizontal+1
        if tablero[Horizontal][randomVertical] == "*" and Horizontal<tamaño:
            while tablero[Horizontal][randomVertical] == "*" and Horizontal<tamaño:
                Horizontal +=1
        while tablero[Horizontal][randomVertical] == ".":
            tablero[Horizontal].pop(randomVertical)
            tablero[Horizontal].insert(randomVertical,"*")
            if Horizontal < tamaño:
                Horizontal +=1
            if tablero[Horizontal][randomVertical] == "*":
                while tablero[Horizontal][randomVertical] == "*" and Horizontal < tamaño:
                    Horizontal +=1

    if randomHorizontal-1 >= 0:
        Horizontal = randomHorizontal-1
        if tablero[Horizontal][randomVertical] == "*" and Horizontal>0:
            while tablero[Horizontal][randomVertical] == "*" and Horizontal>0:
                Horizontal -= 1
        while tablero[Horizontal][randomVertical] == ".":
            tablero[Horizontal].pop(randomVertical)
            tablero[Horizontal].insert(randomVertical,"*")
            if Horizontal > 0:
                Horizontal -= 1
            if tablero[Horizontal][randomVertical] == "*":
                while tablero[Horizontal][randomVertical] == "*" and Horizontal > 0:
                    Horizontal -= 1
    RevisionDiagonal(tamaño,tablero,randomHorizontal,randomVertical)


def RevisionDiagonal(tamaño,tablero,randomHorizontal,randomVertical):
    #Diagonal derecha arriba
    if randomVertical+1 <= tamaño and randomHorizontal-1 >= 0:
        Vertical = randomVertical+1
        Horizontal = randomHorizontal-1
        if tablero[Horizontal][Vertical] == "*" and Horizontal > 0 and Vertical < tamaño:
            while tablero[Horizontal][Vertical] == "*" and Horizontal > 0 and Vertical < tamaño:
                Horizontal -= 1
                Vertical += 1
        while tablero[Horizontal][Vertical] == ".":
            tablero[Horizontal].pop(Vertical)
            tablero[Horizontal].insert(Vertical,"*")
            if Horizontal > 0 and Vertical < tamaño:
                Horizontal -= 1
                Vertical += 1
            if tablero[Horizontal][Vertical] == "*":
                while tablero[Horizontal][Vertical] == "*" and Horizontal > 0 and Vertical < tamaño:
                    Horizontal -= 1
                    Vertical += 1

    #Diagonal izquierda arriba
    if randomVertical-1 >=0 and randomHorizontal-1 >= 0:
        Vertical = randomVertical-1
        Horizontal = randomHorizontal-1
        if tablero[Horizontal][Vertical] == "*" and Horizontal > 0 and Vertical > 0:
            while tablero[Horizontal][Vertical] == "*" and Horizontal > 0 and Vertical > 0:
                Horizontal -= 1
                Vertical -= 1
        while tablero[Horizontal][Vertical] == ".":
            tablero[Horizontal].pop(Vertical)
            tablero[Horizontal].insert(Vertical,"*")
            if Horizontal > 0 and Vertical > 0:
                Horizontal -= 1
                Vertical -= 1
            if tablero[Horizontal][Vertical] == "*":
                while tablero[Horizontal][Vertical] == "*" and Horizontal > 0 and Vertical > 0:
                    Horizontal -= 1
                    Vertical -= 1
    
    #Diagonal derecha abajo
    if randomVertical+1 <= tamaño and randomHorizontal+1 <= tamaño:
        Vertical = randomVertical+1
        Horizontal = randomHorizontal+1
        if tablero[Horizontal][Vertical] == "*" and Horizontal < tamaño and Vertical < tamaño:
            while tablero[Horizontal][Vertical] == "*" and Horizontal < tamaño and Vertical < tamaño:
                Horizontal += 1
                Vertical += 1
        while tablero[Horizontal][Vertical] == ".":
            tablero[Horizontal].pop(Vertical)
            tablero[Horizontal].insert(Vertical,"*")
            if Horizontal < tamaño and Vertical < tamaño:
                Horizontal += 1
                Vertical += 1
            if tablero[Horizontal][Vertical] == "*":
                while tablero[Horizontal][Vertical] == "*" and Horizontal < tamaño and Vertical < tamaño:
                    Horizontal += 1
                    Vertical += 1

    #Diagonal izquierda abajo
    if randomVertical-1 >= 0 and randomHorizontal+1 <= tamaño:
        Vertical = randomVertical-1
        Horizontal = randomHorizontal+1
        if tablero[Horizontal][Vertical] == "*" and Horizontal < tamaño and Vertical > 0:
            while tablero[Horizontal][Vertical] == "*" and Horizontal < tamaño and Vertical > 0:
                Horizontal += 1
                Vertical -= 1
        while tablero[Horizontal][Vertical] == ".":
            tablero[Horizontal].pop(Vertical)
            tablero[Horizontal].insert(Vertical,"*")
            if Horizontal < tamaño and Vertical > 0:
                Horizontal += 1
                Vertical -= 1
            if tablero[Horizontal][Vertical] == "*":
                while tablero[Horizontal][Vertical] == "*" and Horizontal < tamaño and Vertical > 0:
                    Horizontal += 1
                    Vertical -= 1 


def GeneraReinas(reinasG,tamañoG,tablero,Marca):
    i = 1
    contador = 0
    while i <= reinasG or Marca == 1:
        randomHorizontal = random.randint(0,tamañoG)
        randomVertical = random.randint(0,tamañoG)
        if tablero[randomHorizontal][randomVertical] == ".":
            tablero[randomHorizontal].pop(randomVertical)
            tablero[randomHorizontal].insert(randomVertical,"R")
            RevisionHorizonal(tamañoG,tablero,randomHorizontal,randomVertical)  
            i += 1
        else:
            contador+=1
        if contador >= 1000:
            break  
    if Marca == 0:
        ImprimirTablero(tablero,tamañoG,reinasG,i-1)

while True:    
    num_reinas = int(input("Ingresa el numero de reinas: "))
    num_tablero = int(input("Ingresa el tamaño del tablero: "))
    if num_tablero <=0 or num_reinas <=0:
        print("Ingresa nuevamente los datos wei")
    else:
        tablero = [["." for n in range(num_tablero)]for n in range(num_tablero)]
        GeneraReinas(num_reinas, num_tablero-1, tablero,0)