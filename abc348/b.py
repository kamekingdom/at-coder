import math as m

N = int(input())
X, Y = list(), list()
for i in range(N):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

for i, x1, y1 in zip(range(1, N+1), X, Y):
    r_max = float(-1)
    index = -1
    for j, x2, y2 in zip(range(1, N+1), X, Y):
        r_now = m.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if float(r_max) < float(r_now):
            r_max = r_now
            index = j
    print(index)