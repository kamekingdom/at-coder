N = int(input())
A = list(map(int, input().split()))

MOD = 10**8
N = len(A)
total_sum = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        total_sum += (A[i] + A[j]) % MOD
            
print(total_sum)