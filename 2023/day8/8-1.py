paths = {}
with open('8.txt') as f:
    lines = f.readlines()
    steps = lines[0].strip('\n')
    mappings = lines[2:len(lines)]
    for mapping in mappings:
        key = mapping[0:3]
        valueL = mapping[7:10]
        valueR = mapping[12:15]
        paths[key] = (valueL,valueR)

current_location = 'AAA'
num_steps = 0
found = False
while not found:
    for step in steps:
        num_steps +=1
        if step == 'L': current_location = paths[current_location][0]
        elif step == 'R': current_location = paths[current_location][1]
        if current_location == 'ZZZ':
            print(num_steps)
            found=True
            break
