import re

with open('input.txt') as f:
    rows = f.readlines()

rows = [row.strip() for row in rows]

cols = [''.join(list(row)) for row in zip(*rows)]

n = len(rows)
m = len(cols)

diag_up = []
for k in range(0,n+m-1):
    substring = ''
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
             if i + j == k:
                 substring += char
    diag_up.append(substring)


diag_down = []
for k in range(-(m-1),n):
    substring = ''
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
             if i - j == k:
                 substring += char
    diag_down.append(substring)


all = [rows, cols, diag_up, diag_down]


total = 0
for i,l in enumerate(all):
    for text in l:
        matches = re.findall('XMAS',text)
        total+=len(matches)
        matches = re.findall('SAMX',text)
        total+=len(matches)
print(total)
