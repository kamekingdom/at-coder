from collections import deque

def solve(H, W, grid):
    # Convert each string in the grid to a list of characters for mutability
    grid = [list(row) for row in grid]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_reach = 1  # 最小値を1に設定
    
    def print_grid(cx, cy, start, visited):
        for i in range(H):
            row = ''
            for j in range(W):
                if i == cx and j == cy:
                    row += 'o'
                elif i == start[0] and j == start[1]:
                    row += 's'
                elif visited[i][j]:
                    row += 'x'
                else:
                    row += grid[i][j]
            print(row)
        print()  # 空行を出力してグリッド間を区切る

    def bfs(x, y):
        # 隣接するマスに磁石があるかどうかを確認
        if any(grid[x + dx][y + dy] == '#' for dx, dy in directions if 0 <= x + dx < H and 0 <= y + dy < W):
            return 1
        
        visited = [[False] * W for _ in range(H)]
        queue = deque([(x, y)])
        visited[x][y] = True
        reach = 1  # 現在のマスから開始
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '.':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    reach += 1
                    print_grid(nx, ny, (x, y), visited)
                else:
                    grid[cx][cy] = '#'  # ここでマスを塞ぐ
        return reach

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                if not any(grid[i + dx][j + dy] == '#' for dx, dy in directions if 0 <= i + dx < H and 0 <= j + dy < W):
                    result = bfs(i, j)
                    max_reach = max(max_reach, result)
                    print(i+1, j+1, result)

    return max_reach

H, W = list(map(int, input().split()))
S = [input() for _ in range(H)]

print(solve(H, W, S))
