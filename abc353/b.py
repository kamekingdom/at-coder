N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

def check(N, K, A):
    starts = 0
    seats = K
    
    for people in A:
        if people > seats:
            starts += 1
            seats = K 
        
        seats -= people
    
    if seats < K:
        starts += 1
    
    return starts

print(check(N, K, A))