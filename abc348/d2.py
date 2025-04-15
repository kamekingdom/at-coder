# TLE

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

def can_reach(H, W, grid, N, medicines, start, goal):
    medicine_dict = {(r-1, c-1): e for r, c, e in medicines}
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # (row, col, energy)
    
    while queue:
        r, c, energy = queue.popleft()
        if (r, c) == goal:
            return True
        if (r, c, energy) in visited:
            continue
        visited.add((r, c, energy))
        
        if (r, c) in medicine_dict:
            energy = max(energy, medicine_dict[(r, c)])
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and energy > 0:
                queue.append((nr, nc, energy-1))
                
    return False

def main():
    H, W, grid, N, medicines = read_input()
    start, goal = find_start_goal(grid, H, W)
    if can_reach(H, W, grid, N, medicines, start, goal):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
