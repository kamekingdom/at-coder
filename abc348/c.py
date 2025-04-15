
N = int(input())
dic = {}
for i in range(N):
    a, c = list(map(int, input().split()))
    if c not in dic:
        dic[c] = a
    else:
        if dic[c] > a:
            dic[c] = a

print(max(dic.values()))
