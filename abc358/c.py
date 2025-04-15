N, M = list(map(int, input().split()))
S = [input() for _ in range(N)]

class BitManipulation:
    """ビット操作クラス"""

    # positionのビットを1にする
    @staticmethod
    def set_1bit(number, position):
        return number | (1 << position)

    # positionのビットを0にする
    @staticmethod
    def set_0bit(number, position):
        return number & ~(1 << position)

    # positionのビットを反転する
    @staticmethod
    def reverse_bit(number, position):
        return number ^ (1 << position)

    # positionのビットが設定されているかチェックする
    @staticmethod
    def is_bit_exist(number, position):
        return (number & (1 << position)) != 0

    # ビットマスクを適用する
    @staticmethod
    def apply_bitmask(number, mask):
        return number | mask

    # ビットマスクをクリアする
    @staticmethod
    def clear_bitmask(number, mask):
        return number & ~mask

    # nのi桁目が1かをチェックする
    @staticmethod
    def check_1bit(number, digit):
        return number >> digit & 1

    # nのi桁目が0かをチェックする
    @staticmethod
    def check_0bit(number, digit):
        return number >> digit & 0

    # 1の数を数える
    @staticmethod
    def count_1bit(number):
        return bin(number).count('1')

    # digit桁のすべてが1の数を返す(digit = 3 => 111)
    @staticmethod
    def all_1bit(digit):
        return (1 << digit) - 1

    # n桁のすべてが0の数を返す(digit = 3 => 000)
    @staticmethod
    def all_0bit(digit):
        return 0

    # 範囲内のビットを抽出する
    @staticmethod
    def extract_bits(number, high, low):
        mask = (1 << (high - low + 1)) - 1
        return (number >> low) & mask

    # nをa進数からb進数に変換する
    @staticmethod
    def convert_base(number, from_base, to_base):
        number, from_base, to_base = str(number), int(from_base), int(to_base)
        return format(int(number, from_base), 'X' if to_base == 16 else 'o' if to_base == 8 else 'b' if to_base == 2 else 'd' if to_base == 10 else to_base)

    # baseMapのsymbolが1のビットマスクを作成する
    @staticmethod
    def create_bitmask(baseMap, symbol: str):
        N = len(baseMap)
        M = len(baseMap[0]) if N > 0 else 0
        s = [0] * N
        for i in range(N):
            for j in range(M):
                if baseMap[i][j] == str(symbol):
                    s[i] = BitManipulation.set_1bit(s[i], M-1-j)
        return s
bit_func = BitManipulation()

s = bit_func.create_bitmask(S, 'o')

ans = N
# すべての売店に関して全探索
for mask in range(1 << N):
    o = 0
    # i番目の店舗に関して
    for i in range(N):
        # 選択されている場合，
        if bit_func.check_1bit(mask, i):
            # その味を反映する
            o = bit_func.apply_bitmask(o, s[i])
    # もしもすべてが1だったら追加
    if o == bit_func.all_1bit(M):
        ans = min(ans, bit_func.count_1bit(mask))
print(ans)
