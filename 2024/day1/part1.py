list1 = []
list2 = []

with open('input.txt') as f:
    for line in f.readlines():
        s = line.strip().split(' ')
        list1.append(int(s[0]))
        list2.append(int(s[-1]))

total = 0

list1.sort()
list2.sort()

for e1, e2 in zip(list1,list2):
    diff = abs(e1-e2)
    total+=diff

print(total)
