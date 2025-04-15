n = int(input())
L, R = [], []

for _ in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

events = []
for l, r in zip(L, R):
    events.append((l, 's'))
    events.append((r, 'e'))

# 座標圧縮で行けてくれ(懇願)
coords = sorted(set(L + R))
c_map = {v: i for i, v in enumerate(coords)}

max_idx = len(coords)

diff = [0] * (max_idx + 1)

for l in L:
    diff[c_map[l]] += 1
for r in R:
    diff[c_map[r]] -= 1

# 前計算により累積和を計算
current = 0
intersections = 0
active_intervals = 0

for i in range(max_idx):
    current += diff[i]
    if diff[i] > 0:
        intersections += active_intervals * diff[i]
        active_intervals += diff[i]
    elif diff[i] < 0:
        active_intervals += diff[i]

print(intersections)
