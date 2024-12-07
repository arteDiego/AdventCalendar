with open('input_04.txt', 'r') as archivo:
    texto = archivo.read().splitlines()

def comprobar_diagonal_derecha(texto,i,j):
    if(texto[i-1][j-1] == 'M'):
        return(texto[i+1][j+1] == 'S')
    if(texto[i-1][j-1] == 'S'):
        return(texto[i+1][j+1] == 'M')
    return False
    
def comprobar_diagonal_izquierda(texto,i,j):
    if(texto[i-1][j+1] == 'M'):
        return(texto[i+1][j-1] == 'S')
    if(texto[i-1][j+1] == 'S'):
        return(texto[i+1][j-1] == 'M')
    

cont = 0
for i in range(1,len(texto) - 1):
    for j in range(1, len(texto[i]) - 1):
        if texto[i][j] == 'A':
           if(comprobar_diagonal_derecha(texto,i,j) and comprobar_diagonal_izquierda(texto,i,j)):
               cont += 1
                
print(f"Número total de X-MAS: ", cont)