def is_airport_code(S, T):
    n = len(S)
    m = len(T)

    # Tの3番目の文字が'X'の場合のチェック
    if T[2] == 'X':
        found = False
        for i in range(n):
            if S[i].upper() == T[0] and not found:
                for j in range(i+1, n):
                    if S[j].upper() == T[1]:
                        found = True
                        break
        if found:
            return "Yes"
        else:
            return "No"
    else:
        # 通常の3文字のチェック
        index = 0
        for i in range(n):
            if index < 3 and S[i].upper() == T[index]:
                index += 1
            if index == 3:
                return "Yes"
        return "No"

S = input()
T = input()
print(is_airport_code(S, T))
