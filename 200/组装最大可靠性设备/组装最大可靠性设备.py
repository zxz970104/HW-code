# S, N = [int(x) for x in input().split()]
# total = int(input())
# reliability = []
# price = []
# for i in range(total):
#     item = [int(x) for x in input().split()]
#     reliability.append(item[1])
#     price.append(item[2])

S, N = 500, 3
total = 6
info = [
    [[80, 100], [90, 200]], 
    [[50, 50], [70, 210]], 
    [[50, 100], [60, 150]]
]


res = - (1 << 31)
price = 0
curinrel = 1 << 31

def dfs(start, num, curinrel, path):
    global res  # 声明 res 为全局变量
    global price  # 如果需要在函数内修改 price，也需要声明为全局变量
    
    if num == N:  # 注意这里千万不能是start

        # 在最终的一组结果中得到了最小可靠性，并将其与最终的结果比较取较大的
        res = max(res, curinrel)  
        print(path)
        return

    for i in range(start, N):
        for j in range(len(info[i])):
            if price + info[i][j][1] > S:
                continue
            '''
            剪枝优化，
            若i = 2，num = 1, 在这之后 的dfs中 i = 3， num = 2, 没有结果且遍历结束，即这次的dfs毫无作用，可以省去
            这里为何会出现 i != num呢
            原因在于dfs(1, 1, curinrel, path)中，num = 1， 但是当j遍历完成后，i仍会+1变成2，此时i便不再等于num
            '''
            
            # if i != num:
            #     continue

            price += info[i][j][1]
            tmp = curinrel
            curinrel = min(curinrel, info[i][j][0]) # curminrel 记录遍历过程中遇到的最小可靠性

            path.append(info[i][j])

            dfs(i + 1, num + 1, curinrel, path) # 一组里面取完一个后继续在后面的组别取
            path.pop()

            curinrel = tmp
            price -= info[i][j][1]


dfs(0, 0, curinrel, [])
print(res)

