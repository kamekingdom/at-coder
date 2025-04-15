N, A = list(map(int, input().split()))
T = list(map(int, input().split()))

pre = 0
for t in T:
    u = max(t, pre) + A
    print(u)
    pre = u