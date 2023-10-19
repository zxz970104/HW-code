'''
dict.get(key, default=None)
参数说明：

key：要查找的键。
default（可选）：如果键不存在于字典中，则返回这个默认值（默认为None）。
'''

sk = input().split()
s = sk[0]
k = int(sk[1])


# 比较两个字典中0-9数字个数是否相同
def cmp(base, target):
    for c in base:
        if target.get(c) is None or base[c] != target[c]:
            return False
    return True


def getResult():
    target = {}

    # 初始k个数的字典
    for i in range(1, k+1):
        for c in str(i):
            target[c] = target.get(c, 0) + 1
    
    for i in range(k+1, 1000-k+1):
        if cmp(base, target):
            return i-k

        # 去除左边界数字对字典的贡献
        for c in str(i - k):
            target[c] = target.get(c, 0) - 1

        # 添加右边界贡献
        for c in str(i):
            target[c] = target.get(c, 0) + 1


base = {}
for c in s:
    base[c] = base.get(c, 0) + 1

print(getResult())



    

