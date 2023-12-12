import re
from itertools import product

def spring_valid(spring,true_values):
    return [len(damaged) for damaged in re.findall('#+',spring)] == true_values

def generate_springs(spring):
    num_unk = spring.count('?')
    combinations = product('.#',repeat=num_unk)
    springs = []
    for combination in combinations:
        new_spring = ''
        posibilties = iter(combination)
        for char in spring:
            if char == '?':
                new_spring += next(posibilties)
            else:
                new_spring += char
        springs.append(new_spring)
    return springs

with open('12.txt') as f:
    final = 0
    for line in f:
        count = 0
        original_spring, nums = line.split(' ')
        values = list(map(int,re.findall('[0-9]+',nums)))
        for spring in generate_springs(original_spring):
            if spring_valid(spring,values): final+=1
    print(final)
