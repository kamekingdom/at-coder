# DPっぽいな...DPであってくれ...

MOD = 998244353

def lcm(x, y):
    from math import gcd
    return x // gcd(x, y) * y

def solve(N, A, M):
    divisors = [i for i in range(1, M+1) if M % i == 0]
    count = {d: 0 for d in divisors}
    for a in A:
        if a in count:
            count[a] += 1
    
    # DP 初期化
    dp = {d: 0 for d in divisors}
    dp[1] = 1
    
    # DP 更新
    for d in divisors:
        new_dp = dp.copy()
        for x in divisors:
            if dp[x] > 0:
                new_lcm = lcm(x, d)
                if new_lcm in dp:
                    new_dp[new_lcm] = (new_dp[new_lcm] + dp[x]) % MOD
        dp = new_dp
    
    # 組み合わせの数を計算
    result = dp[M]
    for d, cnt in count.items():
        if cnt > 0:
            result = (result * pow(2, cnt, MOD)) % MOD
    
    return result

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
print(solve(N, A, M))
