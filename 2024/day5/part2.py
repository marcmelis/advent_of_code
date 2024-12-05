
before = {}
after = {}
instructions = []


with open('input.txt') as f:
    for line in f.readlines():
        if '|' in line:
            nums = line.strip().split('|')
            n2 = int(nums[1])
            n1 = int(nums[0])
            before[n2] = before.get(n2,[]) + [n1]
        if ',' in line:
            instructions.append([int(num)for num in line.strip().split(',')])


def check(ins):
    for i,num in enumerate(ins):
        if num in before:
            befores = before[num]
            if any([b in ins[i+1:] for b in befores]):
                return False
    return True

def order(ins):
    b = {}
    # generate a new before dict with only the numbers in the instruction
    for k,items in before.items():
        for item in items:
            if k in ins and item in ins:
                b[k] = b.get(k,[]) + [item]
    ordered = []
    # add from the one with less values to the one with the most in the new dict
    for i in range(1,len(b)+1):
        for k in b:
            if len(b[k]) == i:
                for v in b[k]:
                    if v not in ordered:
                        ordered.append(v)
    # add the last one
    for num in ins:
        if num not in ordered:
            ordered.append(num)
    return ordered


total = 0
for ins in instructions:
    if not check(ins):
        ordered = order(ins)
        total += ordered[(len(ins)//2)]

print(total)
