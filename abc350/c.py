# 気持ち：正しいところは visited = True にする

def minimum_swaps_to_sort(N, A):
    A = [a - 1 for a in A] # indexをそろえる用
    visited = [False] * N # 確定の真偽値
    swaps = [] # 履歴

    def process_cycle(start):
        cycle = []
        current = start
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = A[current]
        return cycle

    for i in range(N):
        if not visited[i] and A[i] != i:
            cycle = process_cycle(i)
            for j in range(1, len(cycle)):
                swaps.append((cycle[j - 1] + 1, cycle[j] + 1))

    print(len(swaps))
    for swap in swaps:
        print(*swap)

N = int(input())
A = list(map(int, input().split()))
minimum_swaps_to_sort(N, A)
