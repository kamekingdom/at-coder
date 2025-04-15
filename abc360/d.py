def count_crossings(N, T, S, X):
    count = 0
    
    for i in range(N):
        if S[i] == '1':  # Right moving ant
            for j in range(N):
                if S[j] == '0' and X[i] < X[j] and (X[j] - X[i]) <= 2 * T:
                    count += 1
    
    return count

N, T = map(int, input().split())
S = input().strip()
X = list(map(int, input().split()))

print(count_crossings(N, T, S, X))
