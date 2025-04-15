N, M = list(map(int, input().split()))

MOD = 998244353

backet = [0] * 61

for i in range(61):
    mask = 1 << i
    fulls = N // (mask * 2)
    minds = N % (mask * 2)
    
    backet[i] = fulls * mask
    if minds >= mask:
        backet[i] += minds - mask + 1

result = 0

for i in range(61):
    if M & (1 << i):
        result += backet[i]
        result %= MOD

print(result)