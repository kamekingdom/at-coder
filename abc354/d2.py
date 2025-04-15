def count_black_cells_in_pattern(A, B, C, D):
    # Given rectangle corners (A, B) and (C, D)

    def count_black_in_region(x1, y1, x2, y2):
        total_cells = (x2 - x1 + 1) * (y2 - y1 + 1)
        half_cells = total_cells // 2
        
        if (x1 + y1) % 2 == 0:
            # If the bottom-left corner is black
            black_cells = half_cells + (total_cells % 2)
        else:
            # If the bottom-left corner is white
            black_cells = half_cells
        
        return black_cells

    black_cells = count_black_in_region(A, B, C - 1, D - 1)
    return black_cells * 2

# 入力値を読み込み
A, B, C, D = map(int, input().split())

# 結果を計算して出力
print(count_black_cells_in_pattern(A, B, C, D))
