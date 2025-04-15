def find_remaining_cards(n, strengths, costs):
    # カードを強さとそのインデックスでソート
    indexed_cards = sorted([(i + 1, strengths[i], costs[i]) for i in range(n)], key=lambda x: x[1])
    
    remaining_cards = []
    min_cost = float('inf')
    
    # 強さの昇順でカードをチェック
    for i, strength, cost in indexed_cards:
        # 現在のカードのコストが最小コストよりも小さい場合、残す
        if cost < min_cost:
            remaining_cards.append(i)
            min_cost = cost
    
    # 結果をソートして出力
    remaining_cards.sort()
    return remaining_cards

# 標準入力からの入力を読み込み
N = int(input())
S = []
C = []

for _ in range(N):
    input_value = input().split()
    S.append(int(input_value[0]))
    C.append(int(input_value[1]))

result = find_remaining_cards(N, S, C)
print(len(result))
print(" ".join(map(str, result)))
