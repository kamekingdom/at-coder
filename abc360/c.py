N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

boxes = [0 for _ in range(N)]
boxes_idx = [0 for _ in range(N)]
for i, a in enumerate(A):
    boxes[int(a-1)] += 1
    boxes_idx

moves = list()
for i, box in enumerate(boxes):
    print(box)
    if box >= 2:
        moves.append(i)
    
print(moves)
