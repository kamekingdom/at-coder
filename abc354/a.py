H = int(input())

height = 0
for i in range(10**9):
    height += 2**i
    if H < height:
        print(i+1)
        exit()