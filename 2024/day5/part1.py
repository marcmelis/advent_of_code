
before = {}
instructions = []

with open('input.txt') as f:
    for line in f.readlines():
        if '|' in line:
            nums = line.strip().split('|')
            before[int(nums[1])] = before.get(int(nums[1]),[]) + [int(nums[0])]
        if ',' in line:
            instructions.append([int(num)for num in line.strip().split(',')])


def check(ins):
    for i,num in enumerate(ins):
        if num in before:
            befores = before[num]
            afters = ins[i+1:]
            if any([b in afters for b in befores]):
                return False
    return True


total = 0
for ins in instructions:
    if check(ins):
        total += ins[(len(ins)//2)]

print(total)
