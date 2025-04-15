N = int(input())
events = []

for _ in range(N):
    l, r = map(int, input().split())
    events.append((l, 'L'))
    events.append((r, 'R'))

events.sort(key=lambda x: (x[0], x[1] == 'R'))

active = 0
intersections = 0

for event in events:
    print(intersections)
    if event[1] == 'L':
        intersections += active
        active += 1
    else:
        active -= 1

print(intersections)
