from collections import deque

N = int(input())
A = list(map(int, input().split()))

row = deque()

for a in A:
    row.appendleft(a)
    i = len(row)
    while(1):
        # print(row)
        if len(row) >= 2 and row[0] == row[1]:
            new = row[0]+1
            row.popleft()
            row.popleft()
            row.appendleft(new)
        else:
            break 
        
print(len(row))