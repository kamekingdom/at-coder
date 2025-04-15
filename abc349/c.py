def is_airport_code(S, T):
    index = 0
    if T[2] == "X":
        for str in S:
            if index >= 1:
                return "Yes"
            elif str.lower() == T[index].lower():
                index += 1
    else:
        for str in S:
            if index >= 2:
                return "Yes"
            elif str.lower() == T[index].lower():
                index += 1
    return "No"

S = list(str(input()))
T = list(str(input()))
print(is_airport_code(S, T))