from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

distance_from_exit = [[-1] * W for _ in range(H)]
direction_arrow = [[''] * W for _ in range(H)]

movement_directions = [
    (-1, 0, '^', 'v'),
    (1, 0, 'v', '^'),
    (0, -1, '<', '>'),
    (0, 1, '>', '<')
]

# Add: Exit
search_queue = deque()
for row_index in range(H):
    for column_index in range(W):
        if grid[row_index][column_index] == 'E':
            distance_from_exit[row_index][column_index] = 0
            search_queue.append((row_index, column_index))

# BFS
while search_queue:
    current_row, current_column = search_queue.popleft()
    for delta_row, delta_column, arrow_to_next, arrow_from_next in movement_directions:
        next_row = current_row + delta_row
        next_column = current_column + delta_column

        # Wall or #
        if (
            0 <= next_row < H and
            0 <= next_column < W and
            grid[next_row][next_column] == '.' and
            distance_from_exit[next_row][next_column] == -1
        ):
            distance_from_exit[next_row][next_column] = distance_from_exit[current_row][current_column] + 1
            direction_arrow[next_row][next_column] = arrow_from_next
            search_queue.append((next_row, next_column))

for row_index in range(H):
    output_row = []
    for column_index in range(W):
        if grid[row_index][column_index] == '.':
            output_row.append(direction_arrow[row_index][column_index])
        else:
            output_row.append(grid[row_index][column_index])
    print(''.join(output_row))