N = int(input())
A = list(map(int, input().split()))

MOD = 10**8

print(2 * sum(A) % MOD)
