a, b, c, d, e, f = list(map(int, input().split()))
g, h, i, j, k, l = list(map(int, input().split()))

x_cover = max(a, g) < min(d, j)
y_cover = max(b, h) < min(e, k)
z_cover = max(c, i) < min(f, l)

if x_cover and y_cover and z_cover:
    print("Yes")
else:
    print("No")
