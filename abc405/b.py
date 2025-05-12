N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(N + 1):
    prefix = A[:N - i]
    kinds = set(prefix)
    if any(x not in kinds for x in range(1, M + 1)):
        print(i)
        break