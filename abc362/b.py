pA = list(map(int, input().split()))
pB = list(map(int, input().split()))
pC = list(map(int, input().split()))

def calculate_square(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

dA = calculate_square(pA, pB)
dB = calculate_square(pB, pC)
dC = calculate_square(pC, pA)

sides = sorted([dA, dB, dC])

print("Yes" if (sides[0] + sides[1] == sides[2]) else "No")