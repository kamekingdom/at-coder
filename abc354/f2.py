def min_toll_fee(K, Sx, Sy, Tx, Ty):
    # Calculate how the tile type changes along the path
    def count_changes(pos1, pos2, orthogonal_pos, K):
        # Determine the number of changes along one axis, considering the orthogonal axis position
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1  # Ensure start is always less than end

        # Calculate the initial and final tile types
        initial_tile = ((pos1 // K) + (orthogonal_pos // K)) % 2
        final_tile = ((pos2 // K) + (orthogonal_pos // K)) % 2

        # Count the boundary crossings that result in a change of tile type
        changes = 0
        current_tile = initial_tile
        for pos in range(pos1, pos2 + 1):
            new_tile = ((pos // K) + (orthogonal_pos // K)) % 2
            if pos % K == 0 and new_tile != current_tile:
                changes += 1
                current_tile = new_tile

        return changes

    # Calculate the number of tile type changes in the horizontal and vertical directions
    horizontal_changes = count_changes(Sx, Tx, Sy, K)
    vertical_changes = count_changes(Sy, Ty, Sx, K)

    return horizontal_changes + vertical_changes


K = int(input())
Sx, Sy = list(map(int, input().split()))
Tx, Ty = list(map(int, input().split()))
print(min_toll_fee(K, Sx, Sy, Tx, Ty))
