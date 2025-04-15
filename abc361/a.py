N, K, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A.insert(K, X)

print(*A)