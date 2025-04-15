N, L, R = list(map(int, input().split()))
A = [i+1 for i in range(N)]
A[L-1:R] = A[L-1:R][::-1]
print(*A)
