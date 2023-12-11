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
for i,row in enumerate(galaxy):
    if '#' not in row:
        rows_to_expand.append(i)

# check which cols need expansion
cols_to_expand = []
for i, column in enumerate(zip(*galaxy)):
    if '#' not in column:
        cols_to_expand.append(i)

# get the coordinates summing the expansions
g_coords = []
expansion = 1000000 - 1 # minus the row/col itself
for row_i, row in enumerate(galaxy):
    for col_j, symbol in enumerate(row):
        if symbol == '#':
            extra_row = sum([expansion for row in rows_to_expand if row_i > row])
            extra_col = sum([expansion for col in cols_to_expand if col_j > col])
            g_coords.append((row_i+extra_row,col_j+extra_col))

# compute the manhattan distance
def distance(g1,g2):
    return abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
total = 0
for i,g1 in enumerate(g_coords):
    for g2 in g_coords[i+1:]:
        total+= distance(g1,g2)
print(total)
