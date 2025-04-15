H = int(input())
height = 0
days = 0
while height <= H:
    height = 2**days - 1
    days += 1
print(days-1)