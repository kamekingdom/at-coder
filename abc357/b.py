S = input()

upper_cnt, lower_cnt = 0, 0
for s in S:
    if s == s.lower():
        lower_cnt += 1
    else:
        upper_cnt += 1

ans_list = list()
if upper_cnt > lower_cnt:
    for s in S:
        if s == s.lower():
            ans_list.append(s.upper())
        else:
            ans_list.append(s)
else:
    for s in S:
        if s == s.upper():
            ans_list.append(s.lower())
        else:
            ans_list.append(s)
            
print("".join(ans_list))