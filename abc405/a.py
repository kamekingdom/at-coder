R, X = list(map(int, input().split()))

target_flag = False
if X == 1:
    if 1600 <= R <= 2999:
        target_flag = True
elif X == 2:
    if 1200 <= R <= 2399:
        target_flag = True
print("Yes" if target_flag else "No")