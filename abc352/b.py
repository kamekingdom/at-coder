S = input()
T = input()

ans = []
idx = 0
for i, t in enumerate(T):
    if S[idx] == t:
        idx += 1
        ans.append(i+1)
print(*ans)