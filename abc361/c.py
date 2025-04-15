# 入力の読み込み
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 数列Aをソート
A.sort()
A_len = len(A)

# 最小の差分を求めるための変数
min_diff = float('inf')

# スライディングウィンドウで最小差を探す
for i in range(N - K + 1):
    # print("idx:", i + (N - K) - 1, "idx:",i, )
    if i + (N - K) - 1 >= A_len:
        continue
    else:
        current_diff = A[i + (N - K) - 1] - A[i]
        min_diff = min(min_diff, current_diff)

# 結果の出力
print(min_diff)
