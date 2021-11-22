'''
CSC 425 Artificial Intelligence

Example code for genetic algorithm

Dr. Junxiu Zhou
Fall 2021
'''


import sys
import random

# number of offsprings, you can change it according to your preferences
OFFSPRING_AMT = 10
# step size to stop the code for running infinite loops, you can change it according to your preferences
MAX_STEPS = 10

# cross-over instructions  (e.g., two arithmetic expressions, you can change + to *)
def crossover(parents):
    # cross over parts of code_temp
    code_temp = random.choice(parents)
    code_temp = code_temp.replace("True1", "True")
    return code_temp
# mutate the code (e.g., change the order of the instructions in the code. As the code is ordered line by line,
# you can use a line of code as the mutate target)
def mutate(code_temp):
    # mutate parts of the code_temp
    code_temp = code_temp.replace("False1", "False")
    return code_temp
# use some
def fitness(code_temp):
    score = 0
    # you can use your own test array list
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    #globals() is necessary to define the function globally
    exec(code_temp, globals())
    #test example
    # as we may have "malformed" offspring, we use try clause to keep program runnning without stop the program
    try:
        if(sequentialSearch(testlist, 13) == True):
            score += 1
        if(sequentialSearch(testlist, 130) == False):
            score += 1
        if(sequentialSearch(testlist, 19) == True):
            score += 1
        if(sequentialSearch(testlist, 42) == True):
            score += 1
        if(sequentialSearch(testlist, 81) == False):
            score += 1
        if(sequentialSearch(testlist, 17) == True):
            score += 1
        if(sequentialSearch(testlist, 14) == False):
            score += 1
        if(sequentialSearch(testlist, 1) == True):
            score += 1
        if(sequentialSearch(testlist, 420) == False):
            score += 1
        if(sequentialSearch(testlist, 0) == True):
            score += 1
    except:
        print("Unexpected error:", sys.exc_info())
        score = -1
    return score
# test if the program fulfills the requirements, you can change it accordingly your preferences
def satisfied(codes):
    original_code = """def sequentialSearch(alist, item):
        pos = 0
        found = False
        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos+1
        return found"""
    for str_code in codes:
        if(str_code == original_code):
            print("Found the right code! Exiting!")
            return True
    return False

def main():
    start_code = """def sequentialSearch(alist, item):
        pos = 0
        found = False1
        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True1
            else:
                pos = pos+1
        return found"""
    # parents array
    currParents = []
    # code piece for sequential search (you can change it to other code if you want)
    # use your own strategies to generate initial code pieces as the parents
    # here I just randomly add three original code pieces as the parents seed (Selfing breeding.....)
    currParents.append(start_code)
    offspring = []
    index = 0
    # run until find the target
    while not satisfied(currParents) and index < MAX_STEPS:
        # generate offsprings
        index += 1
        offspring = []
        steps = 0
        while len(offspring) < OFFSPRING_AMT and steps < MAX_STEPS:
            steps += 1
            code_temp = crossover(currParents)
            code_temp = mutate(code_temp)
            #exec(code_temp)
            if(fitness(code_temp) > 5):
                offspring.append(code_temp)
        if len(offspring) >= 1:
            currParents = offspring
    if not satisfied(currParents) and index >= MAX_STEPS:
        print("Could not find correct code")

main()