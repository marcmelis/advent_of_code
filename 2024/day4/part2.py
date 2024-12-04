import re

with open('input.txt') as f:
    rows = f.readlines()

l = [row.strip() for row in rows]

n = len(l)
m = len(l[0])
total=0
for i in range(1,n-1):
    for j in range(1,m-1):
        if l[i][j] == 'A':
            if (l[i-1][j-1] == 'S' and l[i+1][j+1] == 'M') or (l[i-1][j-1] == 'M' and l[i+1][j+1] == 'S'):
                if (l[i-1][j+1] == 'S'and l[i+1][j-1] == 'M') or (l[i-1][j+1] == 'M'and l[i+1][j-1] == 'S'):
                    total+=1
print(total)
