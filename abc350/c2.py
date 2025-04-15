# 気持ち：正しいところは visited = True にする

def minimum_swaps_to_sort(N, A):
    A = [a - 1 for a in A] # indexをそろえる用
    visited = [False] * N # 確定の真偽値
    swaps = [] # 履歴
    
    def check(start):
        print("before", A)
        if A[start] != start:
            tmp = A[start]
            swaps.append((A[tmp]+1, tmp+1))
            visited[A[tmp]] = True
            A[start] = A[A[start]]
            A[tmp] = tmp
        print("after:", A)
    for i in range(N):
        if not visited[i] and A[i] != i:
            check(i)
        print(visited)
        
    print(len(swaps))
    for swap in swaps:
        print(*swap)
            

N = int(input())
A = list(map(int, input().split()))
minimum_swaps_to_sort(N, A)
