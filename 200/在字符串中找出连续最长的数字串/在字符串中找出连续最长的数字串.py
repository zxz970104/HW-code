'''

'''

s = "1234567888890abcd9.+12345.678.9 ed-1239.156"

target_num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
target_sign = ('+', '-')

def solve(string):
    res = [0, 0]
    n = len(string)
    left = 0
    right = 0
    appear_dot = False # 标识是否出现过 .
    appear_sign = False # 标识是否出现过 +-
    while right < n:
        if string[right] in target_num: # 数字
            right += 1
        elif string[right] in target_sign: # +-

            # 之前已经有过+-，当前+-不合法，根据滑动窗口大小更新结果，并重置两个标识
            if appear_sign == True:
                if right - left >= res[1]:
                    res[0] = left
                    res[1] = right - left
                
                right += 1
                left = right
                appear_sign = False
                appear_dot = False
            # 之前未出现+-，当前+-合法标识已出现过+-
            else: 
                left = right
                right += 1
                appear_sign = True
        elif string[right] == '.':  # .

            # 当前 . 合法
            if appear_dot == False and 0 < right < n \
                and string[right-1] in target_num \
                and string[right+1] in target_num:

                right += 1
                appear_dot = True
            # 不合法更新结果，左右指针，标识
            else:
                if right - left >= res[1]:
                    res[0] = left
                    res[1] = right - left
                right += 1
                left = right
                appear_dot = False
                appear_sign = False
        # 其他非法字符，更新结果，指针，标识
        else:
            if right - left >= res[1]:
                res[0] = left
                res[1] = right - left
            right += 1
            left = right
            appear_dot = False
            appear_sign = False

    # 特别注意：若是最后一位也是合法的，最后一次的滑动窗口也要参与更新
    if left < right:
        if right - left >= res[1]:
            res[0] = left
            res[1] = right - left
    return res

res = solve(s)
start = res[0]
end = res[0] + res[1]  # 注意这里不要+1，res[1]是长度，res[0]是起始位置
print(s[start:end])


        
                 

