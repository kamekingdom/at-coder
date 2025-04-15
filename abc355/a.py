A, B = map(int, input().split())
option = {1, 2, 3} - {A, B}
print(option.pop() if len(option) == 1 else -1)
