K = int(input())
C = list(map(int, input().split()))
MOD = 998244353

# # dp[length][used_chars] = length長の文字列を生成するための方法の数
# dp = [[0] * (K + 1) for _ in range(K + 1)]
# dp[0][0] = 1  # 長さ0の文字列は1つ

# # 26文字それぞれについて制約を適用
# for char_limit in C:
#     for length in range(K, -1, -1):
#         for used in range(K, -1, -1):
#             if dp[length][used] > 0:
#                 for add in range(1, char_limit + 1):
#                     if length + add <= K and used + 1 <= K:
#                         dp[length + add][used + 1] = (dp[length + add][used + 1] + dp[length][used]) % MOD

# result = sum(dp[length][used] for length in range(1, K + 1) for used in range(1, K + 1)) % MOD

# print(result)

dp = [[0] * (K + 1) for _ in range(27)]
dp[0][0] = 1

for i in range(26):
    for j in range(K + 1):
        if dp[i][j] == 0:
            continue
        for k in range(C[i] + 1):
            if j + k <= K:
                dp[i + 1][j + k] = (dp[i + 1][j + k] + dp[i][j]) % MOD

result = 0
for length in range(1, K + 1):
    result = (result + dp[26][length]) % MOD

print(result)