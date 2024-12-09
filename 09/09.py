with open('input_09.txt', 'r') as archivo:
    num_str = archivo.read().strip()
    num = [int(digit) for digit in num_str]

def createBase(num):
    ID = 0;
    base = []
    for i in range(len(num)):
        if(i % 2 == 0):
            base.append([ID] * num[i])
            ID += 1;
        else:
            base.append(['.'] * num[i])
    
    base = [elem for row in base for elem in row]
    return base

def swap(base, position1, position2):
    base[position1], base[position2] = base[position2], base[position1]
    return base

def avanzarIndices(base, indexPrincipio, indexFinal):
    while(indexPrincipio < indexFinal and str(base[indexPrincipio]) != '.' ):
        indexPrincipio += 1
    while(base[indexFinal] == '.' and indexFinal > indexPrincipio):
        indexFinal -= 1

    return indexPrincipio, indexFinal

def exchange(base):
    indexPrincipio = 0
    indexFinal = len(base) - 1

    indexPrincipio, indexFinal = avanzarIndices(base,indexPrincipio, indexFinal)

    while(indexPrincipio != indexFinal):
        base = swap(base, indexPrincipio, indexFinal)
        indexPrincipio, indexFinal = avanzarIndices(base, indexPrincipio, indexFinal)

    return base

def checksum(base):
    i = 0
    sum = 0
    while (base[i] != '.'):
        sum += base[i] * i
        i += 1
    return sum


            

base = createBase(num)
base = exchange(base)
sum = checksum(base)
print('El resultado de la suma es: ', sum)