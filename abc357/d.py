# int(list1)*N => N_str
# 1111...を利用できそう...???
# list1に対してmodを効率的に求めたい気持ち
# a^k ≡ b^k <=> a ≡ bを使えないか？
# list1 = 1111... = 1 * 10^k + 1 * 10^k-1 + ... = 10^Nd-1 / 10^d-1
# VN = N * list1

MOD = 998244353
N = int(input().strip())
d = len(str(N))
pow10_d = pow(10, d, MOD)
child = (pow(10, N * d, MOD) - 1 + MOD) % MOD
parent = (pow10_d - 1 + MOD) % MOD
parent_inv = pow(parent, MOD - 2, MOD)
print((N * child * parent_inv) % MOD)