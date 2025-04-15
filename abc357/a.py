N, M = list(map(int, input().split()))
H = list(map(int, input().split()))


left_sanitize = M
for i, h in enumerate(H):
    left_sanitize -= h
    if left_sanitize < 0:
        print(i)
        exit()
print(N)