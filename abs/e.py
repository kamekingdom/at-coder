N = int(input())
A, B = [], []
for i in range(N):
    input_value = list(map(int, input().split()))
    A.append(int(input_value[0]))
    B.append(int(input_value[1]))

cards = list(zip(A, B))

memo = {}

def can_win(state):
    if state in memo:
        return memo[state]
    
    for i in range(N):
        if not (state & (1 << i)):
            continue
        for j in range(i+1, N):
            if not (state & (1 << j)):
                continue
            if cards[i][0] == cards[j][0] or cards[i][1] == cards[j][1]:
                if not can_win(state ^ (1 << i) ^ (1 << j)):
                    memo[state] = True
                    return True
    
    memo[state] = False
    return False

initial_state = (1 << N) - 1
if can_win(initial_state):
    print("Takahashi")
else:
    print("Aoki")

