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
    :return: fila, columna (int, int)
"""




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
        if valor_valido()
