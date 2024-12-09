import numpy as np

matriz = []

with open('input_08.txt', 'r') as archivo:
    for i, line in enumerate(archivo):
        row = list(line.strip())
        matriz.append(row) 

matriz = np.array(matriz)

def obtenerPosiciones(matriz, antena):
    return [(i, j) for i in range(matriz.shape[0]) for j in range(matriz.shape[1]) if matriz[i, j] == antena]

def calcularPosAntinodos(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2

    dr = r2 - r1
    dc = c2 - c1

    antinodo1 = (r1 - dr, c1 - dc) 
    antinodo2 = (r2 + dr, c2 + dc)

    return [antinodo1, antinodo2]

def generarAntinodos(matriz, antenitas, matrizAntinodos):

    for antena in antenitas:
        posiciones = obtenerPosiciones(matriz, antena)

        for i in range(len(posiciones)):
            for j in range(i + 1, len(posiciones)):
                antinodos = calcularPosAntinodos(posiciones[i], posiciones[j])
                for antinodo in antinodos:
                    if (0 <= antinodo[0] < matriz.shape[0] and 0 <= antinodo[1] < matriz.shape[1] and  matrizAntinodos[antinodo[0], antinodo[1]] == '.'):
                        matrizAntinodos[antinodo[0], antinodo[1]] = '#'


    return matrizAntinodos

def contarNumAntinodos(matriz):
    antenitas = np.unique(matriz)[np.unique(matriz) != '.']
    matrizAntinodos = np.full_like(matriz, '.')
    matrizAntinodos = generarAntinodos(matriz, antenitas, matrizAntinodos)

    return np.sum(matrizAntinodos == '#')

resultado = contarNumAntinodos(matriz)
print(f"Número de ubicaciones únicas que contienen antinodos: {resultado}")