N = int(input())
A, B = list(), list()
for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

print(A, B)