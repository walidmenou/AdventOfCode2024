import os

# Get the current working directory
current_dir = os.getcwd()

# Create the path to your input file
input_path = os.path.join(current_dir, "day1", "input1.txt")

def parseInput(filename=input_path):

    list1 = []
    list2 = []
    
    with open(filename, "r") as file:
        for line in file:
            numbers = line.split()
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))
    
    return list1, list2

def findDistance():
    l1, l2 = parseInput()
    
    l1 = sorted(l1)
    l2 = sorted(l2)
    
    res = 0
    for i, j in zip(l1, l2):
        res += abs(i - j)
    
    return res

def findSimilarity():
    l1, l2 = parseInput()

    l1 = sorted(l1)
    l2 = sorted(l2)

    count_l2 = {}

    for n in l2:
        if n in count_l2:
            count_l2[n] += 1
        else:
            count_l2[n] = 1
    
    similarity = 0

    for n in l1:
        if n in count_l2:
            similarity += n*count_l2[n]

    return similarity

print(findSimilarity())