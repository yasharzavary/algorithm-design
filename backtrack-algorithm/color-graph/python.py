# this isn't one backtracking algorithm...it is like backtracking
def validator(m, c, x):
    temp = len(c)
    for i in range(temp):
        if m[temp][i] > 0 and c[i] == x: return False
    return True


def solve(matrix, colors=[], max_color=1):
    x=0
    if len(matrix) == len(colors):return colorsif
    for x in range(max_color):
        if validator(matrix, colors, x):
            return solve(matrix, colors+[x], max_color)
    return solve(matrix, colors+[max_color], max_color+1)

# example one
mat = [
    [0, 1, 1, 1],
    [1, 0, 1, -1],
    [1, 1, 0, 1],
    [1, -1, 1, 0]
]
print(solve(mat))

# example two
mat = [
    [0, 1, -1, -1, -1, -1, -1],
    [1, 0, 1, -1, -1, -1, -1],
    [-1, 1, 0, 1, 1, -1, -1],
    [-1, 1, 1, 0, 1, 1, -1],
    [-1, -1, -1, 1, 0, 1, 1],
    [-1, -1, -1, 1, 1, 0, 1],
    [-1, -1, -1, -1, 1, 1, 0],
    
]
print(solve(mat))