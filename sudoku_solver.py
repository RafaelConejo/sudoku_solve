"""
    Programa capaz de resolver sudokus
    Por Rafael Vázquez Conejo
"""



"""
    Función para encontrar casilla vacía
    :param tablero: lista de int con el tablero
    :return: fila, columna (int, int)
"""
def encontrar_vacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 0:
                return (i, j)

    return None




"""
    Función para validar el valor de una casilla
    :param tablero: lista de int con el tablero
    :param posicion: (fila, columna)
    :param valor: int
    :return: bool
"""
def valor_valido(tablero, posicion, valor):
    salida = True

    #compruebo la fila
    for i in range(0, len(tablero)):
        if(tablero[posicion[0]][i] == valor and posicion[1] != i):
            salida = False

    #compruebo columna
    for i in range(0, len(tablero[0])):
        if(tablero[i][posicion[1]] == valor and posicion[0] != i):
            salida = False

    #Compruebo la caja a la que pertenece
    caja_x = posicion[1]//3
    caja_y = posicion[0]//3

    for i in range(caja_y*3, caja_y*3 + 3):
        for j in range(caja_x*3, caja_x*3 + 3):
            if(tablero[i][j] == valor and (i, j) != posicion):
                salida = False

    return salida


"""
    Resolver mediante backtraking
    :param tablero: lista de int con el tablero
    :return: solucion
"""
def resolver(tablero):
    encontrar = encontrar_vacio(tablero)

    if(find):
        fil, col = find
    else:
        return True

    for i in range(1, 10):
        if valor_valido(tablero, (fil, col), i):
            tablero[fil][col] = i

            if(resolver(tablero)):
                return True

            tablero[fil][col] = 0

    return False
