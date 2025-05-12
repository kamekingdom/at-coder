R, G, B = list(map(int, input().split()))
C = input()

answer = -1
if C == 'Red': answer = min(G, B)
elif C == 'Blue': answer = min(R, G)
elif C == 'Green': answer = min(B, R)

print(answer)