N = int(input())
A, B = [], []
for i in range(N):
    input_value = list(map(int, input().split()))
    A.append(int(input_value[0]))
    B.append(int(input_value[1]))

cards = list(zip(A, B))

memo = {}

def can_win(removed_cards):
    state = tuple(removed_cards)
    if state in memo:
        return memo[state]
    
    for i in range(N):
        if removed_cards[i]:
            continue
        for j in range(i + 1, N):
            if removed_cards[j]:
                continue
            if cards[i][0] == cards[j][0] or cards[i][1] == cards[j][1]:
                new_removed_cards = removed_cards[:]
                new_removed_cards[i] = True
                new_removed_cards[j] = True
                if not can_win(new_removed_cards):
                    memo[state] = True
                    return True
    
    memo[state] = False
    return False

initial_removed_cards = [False] * N
if can_win(initial_removed_cards):
    print("Takahashi")
else:
    print("Aoki")

