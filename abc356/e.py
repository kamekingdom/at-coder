data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# 数列をソート
A.sort()

# 累積和を計算
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + A[i]

result = 0

# ペアの合計値を計算
for i in range(N):
    for j in range(i + 1, N):
        min_val = A[i]
        max_val = A[j]
        result += min_val * (j - i) + prefix_sum[j] - prefix_sum[i + 1]

print(result)