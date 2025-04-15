def divide_interval(L, R):
    intervals = []
    while L < R:
        # 最大の範囲を求める
        largest_power_of_two = 1
        while largest_power_of_two * 2 <= R - L:
            largest_power_of_two *= 2

        # Lがこのべき乗にぴったり収まるように調整
        while (L % largest_power_of_two != 0 or L + largest_power_of_two > R) and largest_power_of_two > 1:
            largest_power_of_two //= 2

        # 次の区間の開始点を計算
        next_L = ((L // largest_power_of_two) + 1) * largest_power_of_two
        if next_L > R:
            next_L = R

        # 新しい区間をリストに追加
        intervals.append((L, next_L))
        L = next_L

    print(len(intervals))
    for start, end in intervals:
        print(start, end)

L, R = list(map(int, input().split()))
divide_interval(L, R)
