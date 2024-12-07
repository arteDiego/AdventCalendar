import numpy as np;
import re;

with open('input_03.txt', 'r') as archivo:
    memoria = archivo.read()

patron = r'mul\((\d+),\s*(\d+)\)'

coincidencias = re.findall(patron, memoria)

sum = 0;

for x,y in coincidencias:
    sum += int(x) * int(y)

print('Suma total de las multiplicaciones: ', sum)

patron_bloques = r'(do\(\)|don\'t\(\))'

bloques = re.split(patron_bloques, memoria);
mul_habilitado = True
sum = 0;

for i in range(0, len(bloques), 2):
    if i > 0:
        accion = bloques[i - 1]
        if accion == 'do()':
            mul_habilitado = True
        elif accion == "don't()":
            mul_habilitado = False

    if mul_habilitado:
        instrucciones = re.findall(patron, bloques[i])
        for x, y in instrucciones:
            sum += int(x) * int(y)

print(bloques[3])
print('Total de multiplicaciones con do() and don\'t()', sum)



