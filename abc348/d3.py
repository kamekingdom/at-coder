# 過去のvisited時のエネルギーレベルが以下である場合に，その位置を訪れないようにする

from collections import deque

def read_input():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    N = int(input())
    medicines = [tuple(map(int, input().split())) for _ in range(N)]
    return H, W, grid, N, medicines

def find_start_goal(grid, H, W):
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'T':
                goal = (i, j)
    return start, goal


def can_reach_optimized(H, W, grid, N, medicines, start, goal):
    medicine_dict = {(r-1, c-1): e for r, c, e in medicines}
    energy_at = {(r, c): -1 for r, c in medicine_dict}  # 各位置における最大のエネルギーレベル
    energy_at[start] = 0
    queue = deque([(*start, 0)])  # (row, col, energy)

    while queue:
        r, c, energy = queue.popleft()
        if (r, c) == goal:
            return True
        
        # 薬を拾う
        if (r, c) in medicine_dict:
            energy = max(energy, medicine_dict[(r, c)])
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and energy > 0:
                # 以前に訪れたことがあり、かつ現在のエネルギー以下ならスキップ
                if energy_at.get((nr, nc), -1) < energy - 1:
                    energy_at[(nr, nc)] = energy - 1
                    queue.append((nr, nc, energy - 1))
    
    return False

def visualize_maze(H, W, grid, path=None):
    """
    迷路とパスを可視化する関数。
    :param H: 迷路の高さ
    :param W: 迷路の幅
    :param grid: 迷路のグリッド
    :param path: オプション、迷路を解くためのパス（(row, col)のリスト）
    :return: None、迷路を出力
    """
    # パスが与えられた場合、迷路にパスを描画
    if path:
        for r, c in path:
            if grid[r][c] not in ('S', 'T'):
                grid[r] = grid[r][:c] + '*' + grid[r][c+1:]

    # 迷路を出力
    for row in grid:
        print(' '.join(row))

H, W, grid, N, medicines = read_input()
start, goal = find_start_goal(grid, H, W)
if can_reach_optimized(H, W, grid, N, medicines, start, goal):
    print("Yes")
else:
    print("No")
