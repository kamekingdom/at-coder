def count_black_cells(A, B, C, D):
    # Adjust coordinates to handle full and partial blocks
    A_adj = (A + 1000000000) % 2
    B_adj = (B + 1000000000) % 2
    C_adj = (C + 1000000000) % 2
    D_adj = (D + 1000000000) % 2

    # Calculate the width and height of the rectangle
    width = C - A
    height = D - B

    # Calculate the number of full 2x2 blocks
    full_blocks = (width // 2) * (height // 2) * 2

    # Initialize black cells count with full blocks contribution
    black_cells = full_blocks

    # Handle remaining columns (partial blocks on the right side)
    if width % 2 != 0:
        for y in range(B, D):
            if (C - 1 + y) % 2 == 0:
                black_cells += 1

    # Handle remaining rows (partial blocks on the top side)
    if height % 2 != 0:
        for x in range(A, C):
            if (x + D - 1) % 2 == 0:
                black_cells += 1

    # Adjust for the bottom-right corner cell if both dimensions have remainders
    if width % 2 != 0 and height % 2 != 0:
        if (C - 1 + D - 1) % 2 == 0:
            black_cells -= 1  # Already counted twice

    return black_cells * 2

# Read input
A, B, C, D = map(int, input().split())

# Calculate and print the result
print(count_black_cells(A, B, C, D))
