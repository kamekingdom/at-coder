from collections import deque

def bfs(x, y, grid, H, W):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 隣接するマスに一つでも磁石がある場合は動けないので終了
    if any(grid[x + dx][y + dy] == '#' for dx, dy in directions if 0 <= x + dx < H and 0 <= y + dy < W):
        print_grid(x, y, x, y, grid, H, W, [[False]*W for _ in range(H)], True)
        return 1
    
    visited = [[False] * W for _ in range(H)]
    queue = deque([(x, y)])
    visited[x][y] = True
    reach = 1  # 現在のマスから開始

    def print_grid(cx, cy, sx, sy, grid, H, W, visited, only_start=False):
        for i in range(H):
            row = ''
            for j in range(W):
                if i == sx and j == sy:
                    row += '@'
                elif i == cx and j == cy:
                    row += 'o'
                elif visited[i][j]:
                    row += 'x'
                else:
                    row += grid[i][j]
            print(row)
        print()  # 空行を出力してグリッド間を区切る

    print_grid(x, y, x, y, grid, H, W, visited)  # 初期位置のグリッド状態を出力

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((nx, ny))
                reach += 1
                print_grid(nx, ny, x, y, grid, H, W, visited)
            else:
                grid[nx][ny] = "#"

    print("Total reachable cells from ({}, {}): {}".format(x + 1, y + 1, reach))
    return reach

# グリッドと位置を設定するための例
H, W = 3, 5
grid = [
    ".#...",
    ".....",
    ".#..#",
]
start_x, start_y = 2, 3  # 1-based index
bfs(start_x - 1, start_y - 1, grid, H, W)  # 0-based index for the function
