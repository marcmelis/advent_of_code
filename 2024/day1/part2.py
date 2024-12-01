list1 = []
list2 = []

with open('input.txt') as f:
    for line in f.readlines():
        s = line.strip().split(' ')
        list1.append(int(s[0]))
        list2.append(int(s[-1]))

total = 0
counts = {}

for e2 in list2:
    counts[e2] = counts.get(e2, 0) + 1

for e1 in list1:
    total += e1*counts.get(e1,0)

print(total)
