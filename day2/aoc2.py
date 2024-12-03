import os

def check(L):
    safe = True
    increasing = True
    decreasing = True
        
    for i in range(len(L) - 1):
        diff = abs(L[i]-L[i+1])

        if diff > 3 or diff < 1:
            safe = False
            
        if L[i] < L[i+1]:
            decreasing = False

        elif L[i] > L[i+1]:
            increasing = False

    if (increasing or decreasing) and safe:
        return True
    
    return False

def evaluateSafety():
    #We need to parse an input of the following format:
    #1 2 3 4
    current_dir = os.getcwd()
    input_path = os.path.join(current_dir, "day2", "input2.txt")
    levels = []
    with open(input_path,'r') as f:
        for line in f:
            numbers = line.split()
            t = []
            for n in numbers:
                t.append(int(n))
            levels.append(t)
        
    res = 0

    for level in levels:

        if check(level):
            res += 1
            continue
        else:
            for i in range(len(level)):
                combination = level[0:i] + level[i+1:]
                #If one combination works then add 
                if check(combination):
                    res += 1
                    break
        
        
    
    print(res)
                

evaluateSafety()