def parse_grid(grid):
    rows, cols = len(grid), len(grid[0])
    graph = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                # 現在のセルのキー
                key = (r, c)
                graph[key] = []
                # 上下左右のセルを確認
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.':
                        graph[key].append((nr, nc))
    return graph

def print_grid(grid, current_pos):
    for r in range(len(grid)):
        row = ""
        for c in range(len(grid[0])):
            if (r, c) == current_pos:
                row += 'o'
            else:
                row += grid[r][c]
        print(row)
    print()  # ステップ間に空行を挿入


# グリッドの定義
grid = [
    ".#...",
    ".....",
    ".#..#"
]

graph = parse_grid(grid)

from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # 訪問ノードの表示

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# DFSの開始位置を指定 (左上のセルから)
# dfs(graph, (0, 0))


def dfs_with_display(graph, start, grid, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # 訪問ノードの表示
    print_grid(grid, start)  # 現在位置を'o'として表示

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_with_display(graph, neighbor, grid, visited)

# DFSの実行
dfs_with_display(graph, (0, 0), grid)