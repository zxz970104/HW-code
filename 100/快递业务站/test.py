class UF:
    def __init__(self, n) -> None:
        self.father = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.num = n # 最初每个节点都是一个连通域
    
    def find(self, x) -> int:
        if x == self.father[x]:
            return x
        else:
            return self.find(self.father[x])
        

    def merge(self, i, j):
        fi = self.find(i)
        fj = self.find(j)
        if self.rank[i] <= self.rank[j]:
            self.father[fi] = fj
        else:
            self.father[fj] = fi
        
        if self.rank[i] == self.rank[j] and fi != fj:
            self.rank[i] += 1

        # 两个节点的父节点不相同且被合并了
        # 那么连通域数量必定会少1
        if fi != fj:
            self.num -= 1
    
    def count(self):
        ret = 0
        for i in range(n):
            if i == self.father[i]:
                ret += 1
        return ret
    
n = int(input())
mat = []
for i in range(n):
    arr = [int(i) for i in input().split()]
    mat.append(arr)

uf = UF(n)

for i in range(n):
    for j in range(i+1, n):
        if mat[i][j] == 1:
            uf.merge(i, j)
print(uf.father)
print(uf.count())
print(uf.num)
        

# 4
# 1 1 1 1
# 1 1 1 0
# 1 1 1 0
# 1 0 0 1

# 4
# 1 1 0 0
# 1 1 0 0
# 0 0 1 0
# 0 0 0 1