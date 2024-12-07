import numpy as np

directions = ('>', '<', '^', 'v')
matriz = []
currentLocation = None 
direction = None

with open('input_06.txt', 'r') as archivo:
    for i, line in enumerate(archivo):
        row = list(line.strip())
        matriz.append(row) 

        if(currentLocation == None):
            for j, char in enumerate(row):
                if char in directions:
                    currentLocation = (i, j)
                    direction = matriz[i][j]

print("\nPrimera ubicación de carácter de dirección:")
print(currentLocation)

matrizRecorrido = np.zeros(shape= np.array(matriz).shape)
row, col = currentLocation
direction = matriz[row][col]

def goForward(currentLocation, direction):
    row, col = currentLocation

    if direction == '>':
        col += 1 
    elif direction == '<':
        col -= 1
    elif direction == '^':
        row -= 1 
    elif direction == 'v':
        row += 1

    return (row, col)

def turnRight(direction):
    if direction == '>':
        direction = 'v'
    elif direction == '<':
        direction = '^'
    elif direction == '^':
        direction = '>'
    elif direction == 'v':
        direction = '<'

    return direction

def markShow(currentLocation, matrizRecorrido):
    row, col = currentLocation
    matrizRecorrido[row][col] = 1
    
    return matrizRecorrido
    
def checkNext(matriz, currentLocation, direction):
    row, col = currentLocation

    num_rows = len(matriz)
    num_cols = len(matriz[0])

    if direction == '>' and col + 1 < num_cols:
        return matriz[row][col + 1] != '#'
    elif direction == '<' and col - 1 >=  0:
        return matriz[row][col - 1] != '#'
    elif direction == '^' and row - 1 >= 0:
        return matriz[row - 1][col] != '#'
    elif direction == 'v' and row + 1 < num_rows:
        return matriz[row + 1][col] != '#'
    return False

def finish(currentLocation, matriz):
    row, col = currentLocation

    num_rows = len(matriz)- 1
    num_cols = len(matriz[0]) - 1
    
    if row <= 0 or row == num_rows or col <= 0 or col == num_cols:
        return True
    return False

def calculateRoute(matriz, start_pos, direction, matrizRecorrido):

    row, col = start_pos
    
    visited = set()

    while True:

        if (row, col, direction) in visited:
            return -1
        visited.add((row, col, direction))
        matrizRecorrido = markShow((row, col), matrizRecorrido)

        if (finish((row, col), matriz)):
            return int(np.sum(matrizRecorrido))

        if checkNext(matriz, (row, col), direction):
            row, col = goForward((row, col), direction)
        else:
            direction = turnRight(direction)

def simulateWithObstacle(matriz, pos):

    matriz_copy = [row[:] for row in matriz]
    row, col = pos
    if matriz_copy[row][col] == '.':
        matriz_copy[row][col] = '#'

        matrizRecorrido = np.zeros(shape=np.array(matriz).shape)
        numCasillas = calculateRoute(matriz_copy, currentLocation, direction, matrizRecorrido)
    
        return numCasillas == -1
    return False

def findLoopPositions(matriz):
    loop_positions = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == '.':
                if simulateWithObstacle(matriz, (i, j)):
                    loop_positions.append((i, j))
    return loop_positions


numCasillas = calculateRoute(matriz, currentLocation, direction, matrizRecorrido)
loop_positions = findLoopPositions(matriz)

print('Numero de casillas distintas recorridas: ', numCasillas)
print(f'Número de posiciones que crean bucles: {len(loop_positions)}')