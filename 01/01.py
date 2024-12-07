import numpy as np

list1 = []
list2 = []

with open('input_01.txt', 'r') as archivo:
    for linea in archivo:
        numero1, numero2 = map(int, linea.split())
        list1.append(numero1)
        list2.append(numero2)

##list1 = [1,2,3,3,3,4];
##list2 = [3,3,3,4,5,9];

list1 = np.sort(list1);
list2 = np.sort(list2);

distance = np.abs(list1 - list2);
totalDistance = np.sum(distance);

print(totalDistance)

similarity = 0;
actualIndex = 0;
dicc = {}

for e in list1 :
    if e not in dicc.keys():
        while actualIndex < len(list2) and list2[actualIndex] < e:
            actualIndex += 1;
        numRep = 0;
        while actualIndex < len(list2) and list2[actualIndex] == e:
            numRep +=1
            actualIndex += 1;
        dicc[e] = e * numRep;
    similarity += dicc[e]

print(similarity)



            
