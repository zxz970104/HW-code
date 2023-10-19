string = input()

def solve(string):
    n = len(string)
    res = 0
    start = 0
    end = 0
    while end < n:
        if string[end].isdigit():
            if start == end: # 重新开始扩展窗口
                end += 1
            else:
                if string[end] >= string[end-1]: 
                    end += 1
                else:
                    res = max(res, end - start) # 注意此时当前end位置处的数字不符合
                    # end += 1， 注意不能end+1，因为此时数字虽不符合，但仍是数字，仍可参与后续的比较
                    start = end 
        else:
            res = max(res, end - start)
            end += 1 # 这里由于不是数字，不能参与后续比较，故需要+1
            start = end
    
    return res

print(solve(string))

