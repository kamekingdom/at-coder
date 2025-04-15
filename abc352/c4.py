N = int(input())
A = list(map(int, input().split()))

def solve(N, A):
    MOD = 10**8
    total_sum = 0
    sum_A = sum(A)  # 全要素の合計

    # 最初から見ていき、各iについて後ろにあるjに対する寄与を計算
    sumAfter = 0  # iより後ろの要素の累積和
    for i in range(N - 1, -1, -1):
        sumAfter += A[i]  # 現在の要素をsumAfterに加える
        total_sum += A[i] * (N - i - 1)  # iより後ろの要素数だけA[i]が足される
        total_sum += sumAfter  # sumAfterには、iより後ろのすべての要素が含まれる
        total_sum %= MOD  # MODで割った余りを保持

    return total_sum

result = solve(N, A)
print(result)
