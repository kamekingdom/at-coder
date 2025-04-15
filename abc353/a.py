N = int(input())
H = list(map(int, input().split()))

def check(H):
    value = H[0]
    for i, h in enumerate(H):
        if value < h:
            return i+1
    return -1
        
print(check(H))
