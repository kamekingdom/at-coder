N, X, Y, Z = list(map(int, input().split()))
if Y < X: X, Y = Y, X
print("Yes" if Z in range(X, Y+1) else "No")