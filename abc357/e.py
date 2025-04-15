N = int(input())
A = list(map(int, input().split()))

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
                self.rank[rootX] += 1

    def get_size(self, x):
        return self.size[self.find(x)]

def solve(N, a):
    uf = UnionFind(N)
    
    for i in range(N):
        uf.union(i, a[i] - 1)
    
    # 全てのグループのサイズをカウント
    component_size = [0] * N
    for i in range(N):
        root = uf.find(i)
        component_size[root] = uf.get_size(root)

    # 各頂点が属するグループのサイズを集計
    group_sizes = {}
    for i in range(N):
        root = uf.find(i)
        if root not in group_sizes:
            group_sizes[root] = uf.get_size(root)
    
    # 到達可能なペアの数をカウント
    total_pairs = 0
    for size in group_sizes.values():
        total_pairs += size * size
    
    return total_pairs

# 結果の出力
print(solve(N, A))
