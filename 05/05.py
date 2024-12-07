dicc = {}
updates = []

with open('input_05.txt', 'r') as archivo:
    texto = archivo.read().splitlines()
    
    for linea in texto:
        if '|' in linea:
            clave, valor = map(int, linea.split('|'))
            if clave not in dicc:
                dicc[clave] = []
            dicc[clave].append(valor)
        elif ',' in linea: 
            updates.append(list(map(int, linea.split(','))))

def comprobar_update(update):
    actual = 0
    while actual < len(update) - 1:
        index = actual + 1
        while index < len(update):
            if update[actual] in dicc.get(update[index], []):
                return False
            index += 1
        actual += 1
    return True

def swap(update, actual, index):
    aux = update[actual];
    update[actual] = update[index]
    update[index] = aux
    return update

def ordenar_update(update):
    actual = 0
    while actual < len(update) - 1:
        index = actual + 1
        while index < len(update):
            if update[actual] in dicc.get(update[index], []):
                update = swap(update, actual, index);
                actual -= 1;
                break
            index += 1
        actual += 1
    return True

def elemento_medio(update):
    middle_index = len(update) // 2
    middle = update[middle_index]
    return middle

sumCorrecto = 0;
sumIncorrecto = 0;

for update in updates:
    if not comprobar_update(update):
        ordenar_update(update);
        sumIncorrecto += elemento_medio(update)
    else:
        sumCorrecto += elemento_medio(update)

print('Numero de la suma total de los updates correctos: ', sumCorrecto)
print('Numero de la suma total de los updates incorrectos: ', sumIncorrecto)


