import numpy as np

with open('input_09_test.txt', 'r') as archivo:
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

def createBaseAndSet(num):
    ID = 0;
    base = []
    set = {}
    for i in range(len(num)):
        if(i % 2 == 0):
            base.append([ID] * num[i])
            set[ID] = num[i]
            ID += 1;
        else:
            base.append(['.'] * num[i])
    
    base = [elem for row in base for elem in row]
    return base, set

def avanzarIndice(base, index):
    while(index < len(base) and str(base[index]) != '.'):
        index += 1;
    indexGap = index
    numGaps = 0;

    while(index < len(base) and str(base[index]) == '.'):
        numGaps += 1
        index += 1
    finish = index >= len(base)


    return indexGap, numGaps, index, finish

def fill(base, indexGap, numGaps, set):
    mod = False
    selectedNum = None
    for num, size in sorted(set.items(), key=lambda x: x[0], reverse=True):
        if size <= numGaps:
            selectedNum = num
            break
   
    if selectedNum is None:
        return base, False

    indexNum = base.index(selectedNum)

    while(indexNum < len(base) and base[indexNum] == selectedNum and indexNum > indexGap):
        mod = True
        base = swap(base, indexGap, indexNum)
        indexGap += 1
        indexNum += 1
    
    del set[selectedNum]

    return base, mod


def fillGaps(base, set):
    index = 0;

    while True:
        nextloop = False
        indexGap, numGaps, index, finish = avanzarIndice(base, index)
        while not finish:
            base, mod = fill(base, indexGap, numGaps, set)
            if(mod):
                nextloop = True
            indexGap, numGaps, index, finish = avanzarIndice(base, index)

        if not nextloop:
            break
    return base


            

base = createBase(num)
base = exchange(base)
sum = checksum(base)
print('El resultado de la suma es: ', sum)

base, set = createBaseAndSet(num)
base = fillGaps(base, set)
sum = checksum(base)
print('El resultado de la suma es: ', sum)