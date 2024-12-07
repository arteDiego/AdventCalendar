import numpy as np

with open('input_07.txt', 'r') as archivo:
    texto = archivo.read().splitlines()


def checkResult(res, nums, operatorArray):
    actualres = nums[0]
    for i in range(len(operatorArray)):
        if operatorArray[i] == 0:
            actualres += nums[i + 1]
        elif operatorArray[i] == 1:
            actualres *= nums[i + 1]
        elif operatorArray[i] == 2:
            actualres = int(str(actualres) + str(nums[i + 1]))

    return actualres == res

def generateCombinations(operators):
    combinations = []
    max_value = 3 ** operators 
    
    for i in range(max_value):
        combination = []
        for _ in range(operators):
            combination.append(i % 3)
            i //= 3 
        
        combinations.append(combination)
    
    return combinations
    

sum = 0;
for line in texto:
    parts = line.split(':')
    res = int(parts[0])
    nums = list(map(int, parts[1].split()))

    operators = len(nums) - 1
    operatorCombinations = generateCombinations(operators)

    found = False;
    for operatorArray in operatorCombinations:
        if checkResult(res, nums, operatorArray):
            found = True;
            break

    if(found):
        sum += res

print('Suma total: ', sum)
    
    
    

   
