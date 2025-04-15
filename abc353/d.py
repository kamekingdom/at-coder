N = int(input())
A = list(map(int, input().split()))

# 桁数を事前に計算
digit_shift = [10**len(str(x)) for x in A]

MOD = 998244353
result = 0

# すべてのペアについて計算
for i in range(N):
    for j in range(i+1, N):
        f_ij = (A[i] * digit_shift[j] + A[j]) % MOD
        result = (result + f_ij) % MOD
        
print(result)