def check(n, strengths, costs):
    # 強さ(A)でソート
    sorted_cards = sorted([(i+1, strengths[i], costs[i]) for i in range(n)], key=lambda x: x[1], reverse=True)
    remaining_cards = []
    min_cost = float('inf')
    # print("sorted cards:",sorted_cards)
    for i, strength, cost in sorted_cards:
        # print("check: ", i, strength, cost)
        if cost < min_cost:
            remaining_cards.append((i))
            min_cost = cost
    remaining_cards.sort()
    return remaining_cards

N = int(input())
S = []
C = []

for _ in range(N):
    input_value = input().split()
    S.append(int(input_value[0]))
    C.append(int(input_value[1]))

result = check(N, S, C)
print(len(result))
print(*result)
