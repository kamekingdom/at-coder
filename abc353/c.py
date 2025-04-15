import itertools

N = int(input())
A = list(map(int, input().split()))

comb = itertools.combinations(range(len(A)), r=2)

def f(x, y):
    return (x+y)%10**8

sum = 0
for i, j in comb:
    sum += f(A[i], A[j])

print(sum)