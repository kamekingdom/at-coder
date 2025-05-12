MOD = 998244353

def prepare_factorials(nmax, mod=MOD):
    fact = [1] * (nmax+1)
    invfact = [1] * (nmax+1)
    for i in range(1, nmax+1):
        fact[i] = fact[i-1] * i % mod
    invfact[nmax] = pow(fact[nmax], mod-2, mod)
    for i in range(nmax, 0, -1):
        invfact[i-1] = invfact[i] * i % mod
    return fact, invfact

def comb(n, k, fact, invfact, mod=MOD):
    if k<0 or k>n: return 0
    return fact[n] * invfact[k] % mod * invfact[n-k] % mod

A, B, C, D = map(int, input().split())
nmax = max(A+B, B+C+D+1)
fact, invfact = prepare_factorials(nmax, MOD)

ans = 0
for i in range(B+1):
    term1 = comb(A+i, A, fact, invfact)
    term2 = comb(B - i + C + D + 1, C, fact, invfact)
    ans = (ans + term1 * term2) % MOD

print(ans)