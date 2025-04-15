N = int(input())

def p_carpet(carpet):
    for c in carpet:
        print("".join(c))
    
carpet = [["#" for i in range(3**N)] for j in range(3**N)]

def check(carpet, x, y, size):
    if size == 1:
        return
    step = size // 3
    for i in range(step, 2*step):
        for j in range(step, 2*step):
            carpet[y + i][x + j] = "."
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                check(carpet, x + i*step, y + j*step, step)

check(carpet, 0, 0, 3**N)
p_carpet(carpet)
