##5
puzzle = ((('⭐', '∞', '-3s', '∞', '+3c', '∞', '+5c'),
           (70, '∞', 5, '∞', 5, '∞', 8),
           ('', '', '', '', '', '', ''),
           (11, '∞', 1, '∞', 2, '∞', 6),
           ('/2s', '∞', '*2c', '∞', '-2s', '∞', 25)),
          (4, 6))

puzzle = list(puzzle)
puzzle.append(False)
puzzle = tuple(puzzle)

m = len(puzzle[0])
n = len(puzzle[0][0])

step = [set()]
step[0].add(puzzle)

all_pos = {puzzle: []}

found = False

def div(a, b):
    s, r = a//b, a%b
    if r*2 >= b:
        return s + 1
    else:
        return s

def walk(cur_pos, direct, board, shield):
    global found
    x, y = cur_pos
    d = x + direct[0], y + direct[1]

    if d[0] not in range(m) or d[1] not in range(n):
        return board, (x, y), shield
    
    b = list(map(list, board))
    o = b[d[0]][d[1]]
    
    if o == '∞':
        return board, (x, y), shield
    
    if o == '⭐':
        found = True
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ''
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split('_')
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        print(b[d[0]][d[1]], len(step) - 1)
        return tuple(map(tuple, b)), d, shield
    
    if o == '':
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ''
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split('_')
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        return tuple(map(tuple, b)), d, shield
    
    if o == 'o':
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ''
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split('_')
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        shield = True
        return tuple(map(tuple, b)), d, shield

    if type(o) is int:
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ''
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split('_')
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        if shield:
            shield = False
        else:
            b[d[0]][d[1]] = b[d[0]][d[1]] - o
            if b[d[0]][d[1]] <= 0:
                return board, (x, y), shield
        return tuple(map(tuple, b)), d, shield
        
    if o[-1] == 'c' and o[0] != '←':
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ''
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split('_')
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        if o[0] == '/':
            b[d[0]][d[1]] = div(b[d[0]][d[1]], int(o[1:-1]))
        elif o[0] == '-':
            b[d[0]][d[1]] = b[d[0]][d[1]] - int(o[1:-1])
        elif o[0] == '+':
            b[d[0]][d[1]] = b[d[0]][d[1]] + int(o[1:-1])
        elif o[0] == '*':
            b[d[0]][d[1]] = b[d[0]][d[1]] * int(o[1:-1])
        elif o[-2] == '/':
            b[d[0]][d[1]] = div(int(o[:-2]), b[d[0]][d[1]])
        elif o[-2] == '-':
            b[d[0]][d[1]] = int(o[:-2]) - b[d[0]][d[1]]
        if b[d[0]][d[1]] <= 0:
            return board, (x, y), shield
        return tuple(map(tuple, b)), d, shield
    
    if o[-1] == 's' and o[0] != '←':
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ''
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split('_')
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        for i in range(m):
            for j in range(n):
                if (i, j) != d and type(b[i][j]) is int:
                    if o[0] == '/':
                        b[i][j] = div(b[i][j], int(o[1:-1]))
                    elif o[0] == '-':
                        b[i][j] = b[i][j] - int(o[1:-1])
                        if b[i][j] < 0:
                            b[i][j] = 0
                    elif o[0] == '+':
                        b[i][j] = b[i][j] + int(o[1:-1])
                    elif o[0] == '*':
                        b[i][j] = b[i][j] * int(o[1:-1])
                    elif o[-2] == '/':
                        b[i][j] = div(int(o[:-2]), b[i][j])
                    elif o[-2] == '-':
                        b[i][j] = int(o[:-2]) - b[i][j]
        return tuple(map(tuple, b)), d, shield

    if o == '←c':
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = int(str(b[x][y])[::-1])
            b[x][y] = ''
        else:
            b[d[0]][d[1]] = int(b[x][y].split('_')[1][::-1])
            b[x][y] = b[x][y].split('_')[0]
        return tuple(map(tuple, b)), d, shield

    if o == '←s':
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ''
        else:
            b[d[0]][d[1]] = int(b[x][y].split('_')[1])
            b[x][y] = b[x][y].split('_')[0]
        for i in range(m):
            for j in range(n):
                if (i, j) != d and type(b[i][j]) is int:
                    b[i][j] = int(str(b[i][j])[::-1])
        return tuple(map(tuple, b)), d, shield
        
    if o[0] in ['>', '<', '=', '≠']:
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ''
        else:
            b[d[0]][d[1]] = int(b[x][y].split('_')[1])
            b[x][y] = b[x][y].split('_')[0]
            
        if o[0] == '>' and b[d[0]][d[1]] > int(o[1:]) or\
           o[0] == '<' and b[d[0]][d[1]] < int(o[1:]) or\
           o[0] == '=' and b[d[0]][d[1]] == int(o[1:]) or\
           o[0] == '≠' and b[d[0]][d[1]] != int(o[1:]):
            b[d[0]][d[1]] = f'{o}_{b[d[0]][d[1]]}'
            b[x][y] = b[x][y].split('_')[0]
            return tuple(map(tuple, b)), d, shield
        else:
            return board, (x, y), shield

    else:
        raise Exception("illegal symbol")
      
    
def l(cur_pos, board, shield):
    return walk(cur_pos, (0, -1), board, shield)

def r(cur_pos, board, shield):
    return walk(cur_pos, (0, 1), board, shield)

def u(cur_pos, board, shield):
    return walk(cur_pos, (-1, 0), board, shield)
    
def d(cur_pos, board, shield):
    return walk(cur_pos, (1, 0), board, shield)

direct_alias = {u: '↑',
                d: '↓',
                r: '→',
                l: '←'}

def bfs():
    while step[-1]:
        step.append(set())
        for p in step[-2]:
            for f in [l, r, u, d]:
                t = f(p[1], p[0], p[2])
                if t not in all_pos:
                    all_pos[t] = all_pos[p][:] + [direct_alias[f]]
                    step[-1].add(t)
                    if found:
                        print(all_pos[t])
                        return
        step[-2].clear() 
    print("not found")

import time
start_time = time.time()
bfs()
print(time.time() - start_time)
