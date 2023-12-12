matrix = []

# read the matrix
with open('day10/10.txt') as f:
    for i,line in enumerate(f):
        matrix.append(list(line.strip('\n')))
        if 'S' in matrix[i]:
            s = (i, matrix[i].index('S'))
# create an empty copy of the matrix to get a clear final pipe
m = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#hardcoded because I know it should be an F
m[s[0]][s[1]] = 'F'


symbol_dict = {
    'N' : { '|': 'N', '7': 'W', 'F': 'E'},
    'S' : { '|': 'S', 'J': 'W', 'L': 'E'},
    'E' : { '-': 'E', 'J': 'N', '7': 'S'},
    'W' : { '-': 'W', 'F': 'S', 'L': 'N'}
}

class Pipe:
    def __init__(self,coords,matrix,in_direction,count):
        self.count = count
        self.v, self.h = coords
        self.matrix = matrix
        self.in_direction = in_direction
        m[self.v][self.h] = matrix[self.v][self.h]
        self.out_direction = symbol_dict[in_direction][matrix[self.v][self.h]]
    def next_Pipe(self):
        if self.out_direction == 'N':
            return Pipe((self.v - 1, self.h),self.matrix,'N',self.count+1)
        elif self.out_direction == 'S':
            return Pipe((self.v + 1, self.h),self.matrix,'S',self.count+1)
        elif self.out_direction == 'E':
            return Pipe((self.v, self.h + 1),self.matrix,'E',self.count+1)
        elif self.out_direction == 'W':
            return Pipe((self.v, self.h - 1),self.matrix,'W',self.count+1)

# Get starting points
s_coords = []
if s[0] != 0 and matrix[s[0]-1][s[1]] in symbol_dict['N'].keys():
    s_coords.append(((s[0]-1,s[1]),'N'))
if s[0] - 1 != len(matrix) and matrix[s[0]+1][s[1]] in symbol_dict['S'].keys():
    s_coords.append(((s[0]+1,s[1]),'S'))
if s[1] != 0 and matrix[s[0]][s[1]-1] in symbol_dict['W'].keys():
    s_coords.append(((s[0],s[1]-1),'W'))
if s[1] - 1 != len(matrix[0])  and matrix[s[0]][s[1]+1] in symbol_dict['E'].keys():
    s_coords.append(((s[0],s[1]+1),'E'))

# Generate starting pipes
s_coords1 = s_coords[0][0]
s_direction1 = s_coords[0][1]
s_coords2 = s_coords[1][0]
s_direction2 = s_coords[1][1]
p1 = Pipe(s_coords1,matrix,s_direction1,1)
p2 = Pipe(s_coords2,matrix,s_direction2,1)

#Iterate through both pipes until they join
while not (p1.h == p2.h and p1.v == p2.v):
    p1 = p1.next_Pipe()
    p2 = p2.next_Pipe()
print(p1.count)
print(p2.count)
