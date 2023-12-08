import math

paths = {}
# Generate paths and steps
with open('8.txt') as f:
    lines = f.readlines()
    steps = lines[0].strip('\n')
    mappings = lines[2:len(lines)]
    for mapping in mappings:
        key = mapping[0:3]
        valueL = mapping[7:10]
        valueR = mapping[12:15]
        paths[key] = (valueL,valueR)

# Find for a single input how much steps it needs to find '**Z'
def find_num_steps(current_location,steps,paths):
    num_steps=0
    while True:
        for step in steps:
            num_steps +=1
            if step == 'L': current_location = paths[current_location][0]
            elif step == 'R': current_location = paths[current_location][1]
            if current_location[-1] == 'Z':
                return num_steps

# Least common multiple
def lcm_two(a,b):
    return abs(a*b) // math.gcd(a,b)

def lcm_multiple(nums):
    lcm = 1
    for num in nums:
        lcm = lcm_two(lcm,num)
    return lcm

locs = [loc for loc in paths.keys() if loc[-1] == 'A']
found = False
first_solution = []
for current_location in locs:
    first_solution.append(find_num_steps(current_location,steps,paths))

# The least common multiple of all the individual solutions 
print(lcm_multiple(first_solution))
