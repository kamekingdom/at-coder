def min_toll_fee(K, Sx, Sy, Tx, Ty):
    def tolls_along_axis(start, end, K):
        # Calculate tolls based on transitions across blocks on one axis
        if start > end:
            start, end = end, start  # Ensure start is less than end

        # Starting and ending blocks
        block_start = start // K
        block_end = end // K

        # Calculate the toll based on crossing from one block to another
        tolls = 0
        for block in range(block_start, block_end):
            start_type = (block + (start // K)) % 2
            end_type = (block + 1 + (start // K)) % 2
            if start_type != end_type:
                tolls += 1
        
        return tolls

    vertical_tolls = tolls_along_axis(Sx, Tx, K)
    horizontal_tolls = tolls_along_axis(Sy, Ty, K)

    return vertical_tolls + horizontal_tolls

K = int(input())
Sx, Sy = list(map(int, input().split()))
Tx, Ty = list(map(int, input().split()))
print(min_toll_fee(K, Sx, Sy, Tx, Ty))
