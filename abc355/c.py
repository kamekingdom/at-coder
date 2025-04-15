N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

row_cnt = [0] * N
col_cnt = [0] * N
diag1_cnt = 0
diag2_cnt = 0

pos = {}
for r in range(N):
    for c in range(N):
        num = N * r + c + 1
        pos[num] = (r, c)

for t in range(T):
    num = A[t]
    if num not in pos:
        continue
    r, c = pos[num]
    row_cnt[r] += 1
    col_cnt[c] += 1
    if r == c:
        diag1_cnt += 1
    if r + c == N - 1:
        diag2_cnt += 1
    
    if row_cnt[r] == N or col_cnt[c] == N or diag1_cnt == N or diag2_cnt == N:
        print(t+1)
        exit()

print(-1)