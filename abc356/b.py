N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

total = [0] * M

for i in range(N):
    for j in range(M):
        total[j] += X[i][j]

for j in range(M):
    if total[j] < A[j]:
        print("No")
        exit()

print("Yes")