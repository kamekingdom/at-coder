N, M, K = map(int, input().split())
conditions = []

for _ in range(M):
    data = input().split()
    Ci = int(data[0])
    A = list(map(int, data[1:1+Ci]))
    Ri = data[1+Ci]
    conditions.append((Ci, A, Ri))

valid_comb = 0

for bit in range(1 << N):
    print("bit", bit)
    is_valid = True
    for Ci, A, Ri in conditions:
        print("Ci", Ci, "A", A, "Ri", Ri)
        count = 0
        for a in A:
            if bit & (1 << (a - 1)):
                count += 1
        if (Ri == 'o' and count < K) or (Ri == 'x' and count >= K):
            is_valid = False
            break
    if is_valid:
        valid_comb += 1

print(valid_comb)