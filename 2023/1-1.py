def first_num(line):
    for c in line:
        if c.isnumeric():
            return c
def last_num(line):
    first_num(line[::-1])


total = 0
with open('data/1-1.txt') as f:
    for line in f:
        total += int(first_num(line) + last_num(line))

print(total)
