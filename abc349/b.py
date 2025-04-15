from collections import Counter

S = input()
count_list = list()
for character, count in Counter(S).items():
    count_list.append(count)

flag = "Yes"
for num, count in Counter(count_list).items():
    if count != 0 and count != 2:
        flag = "No"
        
print(flag)