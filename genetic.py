'''
CSC 425 Artificial Intelligence

Example code for genetic algorithm

Dr. Junxiu Zhou
Fall 2021
'''


import sys
import random
from random import randint

# number of offsprings, you can change it according to your preferences
OFFSPRING_AMT = 1
# step size to stop the code for running infinite loops, you can change it according to your preferences
MAX_STEPS = 100

# cross-over instructions  (e.g., two arithmetic expressions, you can change + to *)
def crossover(parents):
    code_temp = random.choice(parents)
    if randint(0, 10) <= 8:
        if randint(0, 1) == 0:
            #Swap + and - signs
            code_temp = code_temp.replace("+", "PLACEHOLDER")
            code_temp = code_temp.replace("-", "+")
            code_temp = code_temp.replace("PLACEHOLDER", "-")
        if randint(0, 1) == 0:
            #Swap * and / signs
            code_temp = code_temp.replace("*", "PLACEHOLDER")
            code_temp = code_temp.replace("/", "*")
            code_temp = code_temp.replace("PLACEHOLDER", "/")
        if randint(0, 1) == 0:
            #Swap True and False
            code_temp = code_temp.replace("True", "PLACEHOLDER")
            code_temp = code_temp.replace("False", "True")
            code_temp = code_temp.replace("PLACEHOLDER", "False")
    return code_temp
# mutate the code (e.g., change the order of the instructions in the code. As the code is ordered line by line,
# you can use a line of code as the mutate target)
def mutate(code_temp):
    if randint(0,10) < 3:
        code_temp = code_temp.split('\n')
        if randint(0, 1) == 0:
            #move a random line up
            lineNum = randint(1, len(code_temp)-1)
            code_temp[lineNum-1], code_temp[lineNum] = code_temp[lineNum], code_temp[lineNum-1]
        else:
            #move a random line down
            lineNum = randint(0, len(code_temp)-2)
            code_temp[lineNum+1], code_temp[lineNum] = code_temp[lineNum], code_temp[lineNum+1]
        code_temp = '\n'.join(code_temp)
    return code_temp
# use some
def sequential_fitness(code_temp):
    score = 0
    # you can use your own test array list
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    #globals() is necessary to define the function globally
    try:
        exec(code_temp, globals())
    except: #If it can't even define the function return -1
        return -1
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
def sequential_satisfied(codes):
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

def palindrome_satisfied(codes):
    original_code = """def isPalindrome(s):
        newS = ''
        for i in range(len(s)-1, -1, -1):
            newS += s[i]
        if newS == s:
            return True
        else:
            return False"""
    for str_code in codes:
        if(str_code == original_code):
            print("Found the right code! Exiting!")
            return True
    return False

def palindrome_fitness(code_temp):
    score = 0
    #globals() is necessary to define the function globally
    try:
        exec(code_temp, globals())
    except: #If it can't even define the function return -1
        return -1
    #test example
    # as we may have "malformed" offspring, we use try clause to keep program runnning without stop the program
    try:
        if isPalindrome("aba"):
            score += 1
        if not isPalindrome("aab"):
            score += 1
        if isPalindrome("racecar"):
            score += 1
        if not isPalindrome("giraffe"):
            score += 1
        if isPalindrome("a"):
            score += 1
        if isPalindrome("kayak"):
            score += 1
        if not isPalindrome("palindrome"):
            score += 1
    except:
        print("Unexpected error:", sys.exc_info())
        score = -1
    return score

def main():
    random.seed()
    #sequential search start code
    #This code has the else: on the wrong line and is decreasing position rather than increasing
    start_code = """def sequentialSearch(alist, item):
        pos = 0
        found = True
        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = False
                pos = pos-1
            else:
        return found"""

    #palindrome detection start code
    start_code = """def isPalindrome(s):
        newS = ''
        for i in range(len(s)-1, -1, -1):
        if newS == s:
            newS += s[i]
            return False
        else:
            return True"""

    # parents array
    currParents = []
    # code piece for sequential search (you can change it to other code if you want)
    # use your own strategies to generate initial code pieces as the parents
    # here I just randomly add three original code pieces as the parents seed (Selfing breeding.....)
    currParents.append(start_code)
    currParents.append(start_code)
    currParents.append(start_code)
    offspring = []
    index = 0
    # run until find the target
    while not palindrome_satisfied(currParents) and index < MAX_STEPS:
        # generate offsprings
        index += 1
        offspring = []
        steps = 0
        while len(offspring) < OFFSPRING_AMT and steps < MAX_STEPS:
            steps += 1
            code_temp = crossover(currParents)
            code_temp = mutate(code_temp)
            #exec(code_temp)
            if(palindrome_fitness(code_temp) > 5):
                offspring.append(code_temp)
        if len(offspring) >= 1:
            currParents = offspring
    if index >= MAX_STEPS:
        print("Could not find correct code")

    print(f"Total steps: {index}")

main()