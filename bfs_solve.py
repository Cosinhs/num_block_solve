#25
puzzle = (((3, '', '', '∞', '⭐'),
           ('>8', 5, '', '', 30),
           ('/2s', '<9', 2, '', ''),
           ('>10', '*2c', '<10', 4, 12)),
          (3, 4))

m = len(puzzle[0])
n = len(puzzle[0][0])

step = [set()]
step[0].add(puzzle)

all_poss = {puzzle: []}

found = False

def walk(xy, direct, puzzle):
    global found
    x, y = xy
    d = x + direct[0], y + direct[1]
    if d[0] not in range(m) or d[1] not in range(n):
        return puzzle, (x, y)
    p = list(map(list, puzzle))
    o = p[d[0]][d[1]]
    #assert p[x][y] > 0
    if o == '∞':
        return puzzle, (x, y)
    
    if o == '⭐':
        found = True
        if type(p[x][y]) is int:
            p[d[0]][d[1]] = p[x][y]
            p[x][y] = ''
        else:
            p[x][y], p[d[0]][d[1]] = p[x][y].split('_')
            p[d[0]][d[1]] = int(p[d[0]][d[1]])
        print(p[d[0]][d[1]], len(step) - 1)
        return tuple(map(tuple, p)), d
    
    if o == '':
        if type(p[x][y]) is int:
            p[d[0]][d[1]] = p[x][y]
            p[x][y] = ''
        else:
            p[x][y], p[d[0]][d[1]] = p[x][y].split('_')
            p[d[0]][d[1]] = int(p[d[0]][d[1]])
        return tuple(map(tuple, p)), d
    
    if type(o) is int:
        if type(p[x][y]) is int:
            p[d[0]][d[1]] = p[x][y] - o
            if p[d[0]][d[1]] <= 0:
                return puzzle, (x, y)
            p[x][y] = ''
        else:
            p[d[0]][d[1]] = int(p[x][y].split('_')[1])
            p[d[0]][d[1]] = p[d[0]][d[1]] - o
            if p[d[0]][d[1]] <= 0:
                return puzzle, (x, y)
            p[x][y] = p[x][y].split('_')[0]
        return tuple(map(tuple, p)), d
    
    if o[-1] == 'c':
        if type(p[x][y]) is int:
            if o[0] == '/':
                p[d[0]][d[1]] = round(p[x][y] / int(o[1:-1]))
            else:
                p[d[0]][d[1]] = eval(f'{p[x][y]}{o[:-1]}')
            if p[d[0]][d[1]] <= 0:
                return puzzle, (x, y)
            p[x][y] = ''
        else:
            p[d[0]][d[1]] = int(p[x][y].split('_')[1])
            if o[0] == '/':
                p[d[0]][d[1]] = round(p[d[0]][d[1]] / int(o[1:-1]))
            else:
                p[d[0]][d[1]] = eval(f'{p[d[0]][d[1]]}{o[:-1]}')
            if p[d[0]][d[1]] <= 0:
                return puzzle, (x, y)
            p[x][y] = p[x][y].split('_')[0]
        return tuple(map(tuple, p)), d
    
    if o[-1] == 's':
        if type(p[x][y]) is int:
            p[d[0]][d[1]] = p[x][y]
            p[x][y] = ''
        else:
            p[d[0]][d[1]] = int(p[x][y].split('_')[1])
            p[x][y] = p[x][y].split('_')[0]
        for i in range(m):
            for j in range(n):
                if (i, j) != d and type(p[i][j]) is int:
                    if o[0] == '/':
                        p[i][j] = round(p[i][j] / int(o[1:-1]))
                    else:
                        p[i][j] = eval(f'{p[i][j]}{o[:-1]}')
        return tuple(map(tuple, p)), d
    
    if o[0] == '>':
        if type(p[x][y]) is int:
            if p[x][y] > int(o[1:]):
                p[d[0]][d[1]] = f'{o}_{p[x][y]}'
                p[x][y] = ''
                return tuple(map(tuple, p)), d
            else:
                return puzzle, (x, y)
        else:
            p[d[0]][d[1]] = int(p[x][y].split('_')[1])
            if p[d[0]][d[1]] > int(o[1:]):
                p[d[0]][d[1]] = f'{o}_{p[d[0]][d[1]]}'
                p[x][y] = p[x][y].split('_')[0]
                return tuple(map(tuple, p)), d
            else:
                return puzzle, (x, y)
        
    if o[0] == '<':
        if type(p[x][y]) is int:
            if p[x][y] < int(o[1:]):
                p[d[0]][d[1]] = f'{o}_{p[x][y]}'
                p[x][y] = ''
                return tuple(map(tuple, p)), d
            
            else:
                return puzzle, (x, y)
        else:
            p[d[0]][d[1]] = int(p[x][y].split('_')[1])
            if p[d[0]][d[1]] < int(o[1:]):
                p[d[0]][d[1]] = f'{o}_{p[x][y]}'
                p[x][y] = p[x][y].split('_')[0]
                return tuple(map(tuple, p)), d
            
            else:
                return puzzle, (x, y)
            
    if o[0] == '=':
        if type(p[x][y]) is int:
            if p[x][y] == int(o[1:]):
                p[d[0]][d[1]] = f'{o}_{p[x][y]}'
                p[x][y] = ''
                return tuple(map(tuple, p)), d
            else:
                return puzzle, (x, y)
        else:
            p[d[0]][d[1]] = int(p[x][y].split('_')[1])
            if p[d[0]][d[1]] == int(o[1:]):
                p[d[0]][d[1]] = f'{o}_{p[x][y]}'
                p[x][y] = p[x][y].split('_')[0]
                return tuple(map(tuple, p)), d
            
            else:
                return puzzle, (x, y)
        
def l(xy, puzzle):
    return walk(xy, (0, -1), puzzle)

def r(xy, puzzle):
    return walk(xy, (0, 1), puzzle)

def u(xy, puzzle):
    return walk(xy, (-1, 0), puzzle)
    
def d(xy, puzzle):
    return walk(xy, (1, 0), puzzle)

direct_alias = {u: '↑',
                d: '↓',
                r: '→',
                l: '←'}

def bfs():
    while 1:
        step.append(set())
        for p in step[-2]:
            for f in [l, r, u, d]:
                t = f(p[1], p[0])
                if t not in all_poss:
                    all_poss[t] = all_poss[p][:] + [direct_alias[f]]
                    step[-1].add(t)
                if found:
                    print(all_poss[t])
                    return
        step[-2].clear()
                
bfs()
