N = int(input())
A = list(map(int, input().split()))

# MOD = 10**8
MOD = 10**8

sum_A = sum(A) * (N-1)

print(sum_A)

cnt = [0]*(MOD+1)
for a in A:
    cnt[a] += 1

# 累積和
for i in range(MOD):
    cnt[i+1] += cnt[i]

print(sum_A - (N - cnt[MOD]))