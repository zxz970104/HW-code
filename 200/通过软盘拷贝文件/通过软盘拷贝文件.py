N = int(input())
files = []

# 构建文件实际大小与需要占用的大小
for i in range(N):
    size = int(input())
    if size % 512 == 0: # 可除尽，实际大小与占用大小相同
        true_size = size 
    else:
        k = size >> 9 # 移位操作符效率更高，得到商
        true_size = (k+1) << 9
    files.append([true_size, size])

files.sort()
print(files)
max_size = 1474560
res = 0
full = False # 标记是否刚好装满，是的话他就是最佳答案，后续回溯便不需要进行了

def dfs(start, total_size, total_true_size):
    global res
    global full

    if full:
        return
    
    for i in range(start, N):
        # 剪枝，加上本次循环占用空间已超过磁盘空间，由于从小到大排序，后续的也不用回溯了
        if total_true_size + files[i][0] > max_size:
            # 注意在这里更新答案
            res = max(total_size, res) 
            return
        # 刚好装满
        if total_true_size + files[i][0] == max_size and total_size + files[i][1] == max_size:
            res = max_size
            full = True
            return
        total_true_size += files[i][0]
        total_size += files[i][1]

        dfs(i+1, total_size, total_true_size)

        total_true_size -= files[i][0]
        total_size -= files[i][1]


print(dfs(0, 0, 0))
print(res)

'''
3
737270
737272
737288

6
400000
200000
200000
200000
400000
400000
'''