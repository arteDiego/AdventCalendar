import numpy as np;

reports = [];
with open('input_02.txt', 'r') as archivo:
    for linea in archivo:
        line_numbers = list(map(int, linea.split()))
        reports.append(line_numbers)

def comprobarLista(register):
    index = 0;
    size = np.size(register);

    if(register[1] > register[0]):
        while index < size:
            if(index == size - 1):
                return -1
            else:
                if(register[index + 1] - register[index] > 3 or register[index + 1] - register[index] < 1):
                    return index
            index += 1
        
    else:
        while index < size:
            if(index == size - 1):
                return -1
            else:
                if(register[index] - register[index + 1] > 3 or register[index] - register[index + 1] < 1):
                    return index
            index += 1

cont = 0;
for register in reports:
    register = np.array(register).flatten()
    index = comprobarLista(register)
    if(index == -1):
        cont += 1;
    else:   
        register2 = np.delete(register, index);
        register1 = np.delete(register, index - 1);
        register3 = np.delete(register, index + 1);
        if(comprobarLista(register1) == -1 or comprobarLista(register2) == -1 or comprobarLista(register3) == -1):
            cont += 1;

print('Numero total de regsitros correctos: ', cont)
