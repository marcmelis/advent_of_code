galaxy = []

# generate galaxy
with open('11.txt') as f:
    lines = f.readlines()
    galaxy_rows = len(lines)
    galaxy_cols = len(lines[0])
    for line in lines:
        line = line.strip('\n')
        galaxy.append(list(line))

# check which rows need expansion
rows_to_expand = []
overhead = 0
for i,row in enumerate(galaxy):
    if '#' not in row:
        rows_to_expand.append(i+overhead)
        overhead+=1

# check which cols need expansion
columns_to_expand = []
overhead = 0
for i, column in enumerate(zip(*galaxy)):
    if '#' not in column:
        columns_to_expand.append(i+overhead)
        overhead+=1

# expand rows
for row in rows_to_expand:
    galaxy.insert(row,['.' for _ in range(galaxy_rows)])

# expand cols
for row_i,row in enumerate(galaxy):
    for col_i in columns_to_expand:
        row.insert(col_i,'.')

# get galaxies coords on new expanded galaxy
g_coords = []
for row_i, row in enumerate(galaxy):
    for col_j, symbol in enumerate(row):
        if symbol == '#':
            g_coords.append((row_i,col_j))

# compute distances
def distance(g1,g2):
    return abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
total = 0
for i,g1 in enumerate(g_coords):
    for g2 in g_coords[i+1:]:
        total+= distance(g1,g2)
print(total)
