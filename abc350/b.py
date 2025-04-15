from collections import Counter

N, Q = list(map(int, input().split()))
T = list(map(int, input().split()))

T_counter = Counter(T)

odd_num = 0
for t, count in T_counter.items():
    if count%2 != 0:
        odd_num += 1
        
print(N-odd_num)