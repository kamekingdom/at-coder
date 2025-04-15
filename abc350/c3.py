def minimum_swaps_to_sort(N, A):
    swaps = []
    i = 0
    while i < N:
        correct_position = A[i] - 1
        if correct_position != i:
            # 元々の位置に正しい数字を置くためにスワップ
            A[i], A[correct_position] = A[correct_position], A[i]
            swaps.append((i + 1, correct_position + 1))  # 1-indexed
            # iを増やさないで再度確認
        else:
            i += 1
    # 結果出力
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

N = int(input())
A = list(map(int, input().split()))
minimum_swaps_to_sort(N, A)