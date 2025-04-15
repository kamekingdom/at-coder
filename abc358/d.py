# 入力の読み込み
N, M = map(int, input().split())  # N: 箱の数, M: 人の数
A = list(map(int, input().split()))  # A[i]: 箱iの価格
B = list(map(int, input().split()))  # B[i]: 人iに渡すべきお菓子の数

# お菓子の数が多い順にBをソート
B_sorted = sorted(B)

# Aの箱の価格とお菓子の数をペアにしてソート
boxes = sorted(zip(A, range(N)))

# 価格の合計の初期化
total = 0
j = 0

# B_sortedの各値についてループ
for b in B_sorted:
    # 箱の価格がbより小さい限りインデックスを進める
    while j < N and boxes[j][0] < b:
        j += 1
    # 条件を満たす箱が見つかったら合計値に価格を追加
    if j < N:
        total += boxes[j][0]
        j += 1
    else:
        print(-1)
        exit()

print(total)
