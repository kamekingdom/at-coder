def max_profit(N, C, M, markets):
    # タプル(Ti, Pi)を市場が開催される町Tiに基づいてソート
    markets.sort()

    # dp[i]は、i番目の町にいるときの最大所持金額を表す
    dp = [-float('inf')] * (N + 1)
    dp[1] = 10**100  # 初期所持金額

    current_market = 0
    # 各市場を順番に処理
    for market in range(M):
        T, P = markets[market]
        # 市場が開催される町に最も近い前の市場を探す
        while current_market < market and markets[current_market][0] < T:
            current_market += 1

        # 前の市場から現在の市場への最適な移動を計算
        for i in range(1, N + 1):
            if dp[i] != -float('inf'):
                # 移動コストを計算
                cost = C * abs(T - i)
                # 新しい所持金額を計算して、必要であれば更新
                new_money = dp[i] - cost + P
                if new_money > dp[T]:
                    dp[T] = new_money

    # 最大所持金額を計算
    max_money = max(dp)
    return max_money - 10**100  # 初期値を差し引く