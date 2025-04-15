# 最適に行動するとは...？？

def check_vhd(board):
    # Check horizontal and vertical lines
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return "Takahashi" if board[i][0] == 'R' else "Aoki"
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return "Takahashi" if board[0][i] == 'R' else "Aoki"

    # Check diagonal lines
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return "Takahashi" if board[0][0] == 'R' else "Aoki"
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return "Takahashi" if board[0][2] == 'R' else "Aoki"

    # If no winner yet
    return None

board =  [input().split() for _ in range(3)]
print(check_vhd(board))