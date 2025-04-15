N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = sorted(A + B)

count = 0
ans = "No"
for c in C:
    count = count + 1 if c in A else 0
    if count >= 2:
        ans = "Yes"
        break

print(ans)
