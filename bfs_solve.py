import sys
import rapidjson

##23
puzzle = ((('⭐', '∞', '', '/10c', '/10c'),
           ('=113', 1, '', '*10c', '*10c'),
           ('', '', '', '*3c', '*3c'),
           ('*3c', '+1c', '+4c', '', '*4c')),
          (1, 1))

m = len(puzzle[0])
n = len(puzzle[0][0])

puzzle += (False, )
puzzle = rapidjson.dumps(puzzle)

step = [set()]
step[0].add(puzzle)

all_pos = {puzzle: ""}

found = False

def div(a, b):
    s, r = a//b, a%b
    if r*2 >= b:
        return s + 1
    else:
        return s

def walk(board, direct):
    global found
    
    board = rapidjson.loads(board)
    b = board[0]
    x, y = board[1]
    shield = board[2]
    d = x + direct[0], y + direct[1]

    if d[0] not in range(m) or d[1] not in range(n):
        return None

    o = b[d[0]][d[1]]
    
    if o == "∞":
        return None
    
    if o == "⭐":
        found = True
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ""
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split("_")
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        print(b[d[0]][d[1]], len(step) - 1)
        return sys.intern(rapidjson.dumps([b, d, shield]))
    
    if o == "":
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ""
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split("_")
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        return sys.intern(rapidjson.dumps([b, d, shield]))
    
    if o == "o":
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ""
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split("_")
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        shield = True
        return sys.intern(rapidjson.dumps([b, d, shield]))

    if type(o) is int:
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ""
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split("_")
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        if shield:
            shield = False
        else:
            b[d[0]][d[1]] = b[d[0]][d[1]] - o
            if b[d[0]][d[1]] <= 0:
                return None
        return sys.intern(rapidjson.dumps([b, d, shield]))
        
    if o[-1] == "c" and o[0] != "←":
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ""
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split("_")
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        if o[0] == "/":
            b[d[0]][d[1]] = div(b[d[0]][d[1]], int(o[1:-1]))
        elif o[0] == "-":
            b[d[0]][d[1]] = b[d[0]][d[1]] - int(o[1:-1])
        elif o[0] == "+":
            b[d[0]][d[1]] = b[d[0]][d[1]] + int(o[1:-1])
        elif o[0] == "*":
            b[d[0]][d[1]] = b[d[0]][d[1]] * int(o[1:-1])
        elif o[-2] == "/":
            b[d[0]][d[1]] = div(int(o[:-2]), b[d[0]][d[1]])
        elif o[-2] == "-":
            b[d[0]][d[1]] = int(o[:-2]) - b[d[0]][d[1]]
        if b[d[0]][d[1]] <= 0:
            return None
        return sys.intern(rapidjson.dumps([b, d, shield]))
    
    if o[-1] == "s" and o[0] != "←":
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ""
        else:
            b[x][y], b[d[0]][d[1]] = b[x][y].split("_")
            b[d[0]][d[1]] = int(b[d[0]][d[1]])
        for i in range(m):
            for j in range(n):
                if (i, j) != d and type(b[i][j]) is int:
                    if o[0] == "/":
                        b[i][j] = div(b[i][j], int(o[1:-1]))
                    elif o[0] == "-":
                        b[i][j] = b[i][j] - int(o[1:-1])
                        if b[i][j] < 0:
                            b[i][j] = 0
                    elif o[0] == "+":
                        b[i][j] = b[i][j] + int(o[1:-1])
                    elif o[0] == "*":
                        b[i][j] = b[i][j] * int(o[1:-1])
                    elif o[-2] == "/":
                        b[i][j] = div(int(o[:-2]), b[i][j])
                    elif o[-2] == "-":
                        b[i][j] = int(o[:-2]) - b[i][j]
                        if b[i][j] < 0:
                            b[i][j] = 0
        return sys.intern(rapidjson.dumps([b, d, shield]))

    if o == "←c":
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = int(str(b[x][y])[::-1])
            b[x][y] = ""
        else:
            b[d[0]][d[1]] = int(b[x][y].split("_")[1][::-1])
            b[x][y] = b[x][y].split("_")[0]
        return sys.intern(rapidjson.dumps([b, d, shield]))

    if o == "←s":
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ""
        else:
            b[d[0]][d[1]] = int(b[x][y].split("_")[1])
            b[x][y] = b[x][y].split("_")[0]
        for i in range(m):
            for j in range(n):
                if (i, j) != d and type(b[i][j]) is int:
                    b[i][j] = int(str(b[i][j])[::-1])
        return sys.intern(rapidjson.dumps([b, d, shield]))
        
    if o[0] in [">", "<", "=", "≠"]:
        if type(b[x][y]) is int:
            b[d[0]][d[1]] = b[x][y]
            b[x][y] = ""
        else:
            b[d[0]][d[1]] = int(b[x][y].split("_")[1])
            b[x][y] = b[x][y].split("_")[0]
            
        if o[0] == ">" and b[d[0]][d[1]] > int(o[1:]) or \
           o[0] == "<" and b[d[0]][d[1]] < int(o[1:]) or \
           o[0] == "=" and b[d[0]][d[1]] == int(o[1:]) or \
           o[0] == "≠" and b[d[0]][d[1]] != int(o[1:]):
            b[d[0]][d[1]] = f"{o}_{b[d[0]][d[1]]}"
            b[x][y] = b[x][y].split("_")[0]
            return sys.intern(rapidjson.dumps([b, d, shield]))
        else:
            return None

    else:
        raise Exception(f"illegal symbol at {d}")


def l(board):
    return walk(board, (0, -1))

def r(board):
    return walk(board, (0, 1))

def u(board):
    return walk(board, (-1, 0))
    
def d(board):
    return walk(board, (1, 0))

direct_alias = {u: "↑",
                d: "↓",
                r: "→",
                l: "←"}

def bfs():
    while step[-1]:
        step.append(set())
        for p in step[-2]:
            for f in [l, r, u, d]:
                t = f(p)
                if t is None:
                    continue
                if t not in all_pos:
                    all_pos[t] = sys.intern(all_pos[p] + direct_alias[f])
                    step[-1].add(t)
                    if found:
                        print(list(all_pos[t]))
                        return
        step[-2].clear() 
    print("not found")

import time
start_time = time.time()
bfs()
print(time.time() - start_time)
