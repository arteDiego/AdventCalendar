with open('input_04.txt', 'r') as archivo:
    texto = archivo.read().splitlines()

def comprobar_horizontal(texto, i,j) :
    if j + 3 < len(texto[i]):
        return(texto[i][j+1] == 'M' and texto[i][j+2] == 'A' and texto[i][j+3] == 'S')
    return False

def comprobar_horizontal_reves(texto, i,j) :
    if j - 3 >= 0:
        return(texto[i][j-1] == 'M' and texto[i][j-2] == 'A' and texto[i][j-3] == 'S')
    return False

def comprobar_vertical(texto, i, j):
    if i + 3 < len(texto):
        return (texto[i+1][j] == 'M' and texto[i+2][j] == 'A' and texto[i+3][j] == 'S')
    return False

def comprobar_vertical_reves(texto, i, j):
    if i - 3 >= 0:
        return (texto[i-1][j] == 'M' and texto[i-2][j] == 'A' and texto[i-3][j] == 'S')
    return False

def comprobar_diagonal_derecha(texto, i, j):
    if i + 3 < len(texto) and j + 3 < len(texto[i]):
        return (texto[i+1][j+1] == 'M' and texto[i+2][j+2] == 'A' and texto[i+3][j+3] == 'S')
    return False

def comprobar_diagonal_izquierda(texto, i, j):
    if i + 3 < len(texto) and j - 3 >= 0:
        return (texto[i+1][j-1] == 'M' and texto[i+2][j-2] == 'A' and texto[i+3][j-3] == 'S')
    return False

def comprobar_diagonal_reves(texto, i, j):
    if i - 3 >= 0 and j - 3 >= 0:
        return (texto[i-1][j-1] == 'M' and texto[i-2][j-2] == 'A' and texto[i-3][j-3] == 'S')
    return False

def comprobar_diagonal_reves_derecha(texto, i, j):
    if i - 3 >= 0 and j + 3 < len(texto[1]):
        return (texto[i-1][j+1] == 'M' and texto[i-2][j+2] == 'A' and texto[i-3][j+3] == 'S')
    return False

cont = 0
for i in range(len(texto)):
    for j in range(len(texto[i])):
        if texto[i][j] == 'X':
            cont += (
                comprobar_horizontal(texto, i, j) +
                comprobar_horizontal_reves(texto, i, j) +
                comprobar_vertical(texto, i, j) +
                comprobar_vertical_reves(texto, i, j) +
                comprobar_diagonal_derecha(texto, i, j) +
                comprobar_diagonal_izquierda(texto,i,j) +
                comprobar_diagonal_reves_derecha(texto,i,j) +
                comprobar_diagonal_reves(texto, i, j)
            )
                
print(f"Número total de XMAS: ", cont)





