#    0123456789
S = "efgg|abccd"

# 全部分割
print(list(S))
# 指定文字で分割
print(S.split("|"))

# 指定文字列を指定文字列に置換
print(S.replace("efgg", "egg"))

# ｎ文字目取得
print(S[1])
# 最後の文字取得
print(S[-1])
# 間の文字列取得
print(S[3:5+1])

# 文字列検索(前向き)
print(S.find("gg"))
# 文字列検索(後ろ向き)
print(S.rfind("ccd"))