S, T = list(input().split())

lenS = len(S)
lenT = len(T)

for w in range(1, lenS):
    for c in range(1, w + 1):
        result = []
        for i in range(0, lenS, w):
            part = S[i:i+w]
            if len(part) >= c:
                result.append(part[c-1])
        s = ''.join(result)
        # print(s)
        if s == T:
            print("Yes")
            exit()
print("No")

