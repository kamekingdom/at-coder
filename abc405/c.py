N = int(input())
A = list(map(int, input().split()))

total = sum(A)
squared_sum = sum(x * x for x in A)

answer = (total * total - squared_sum) // 2
print(answer)
