from collections import deque

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



def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)
        print(vertex)  # 訪問ノードの表示

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

def bfs_with_display(graph, start, grid):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)
        print(vertex)  # 訪問ノードの表示
        print_grid(grid, vertex)  # 現在位置を'o'として表示

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

# BFSの実行
bfs_with_display(graph, (0, 0), grid)