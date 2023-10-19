num = input()
import re

def check(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != '0':
            return False
        if i % 2 == 1 and s[i] != '1':
            return False
    return True


def solve(num):
    q = []  # 栈中保存一个完整的信号
    reg = re.compile("^(01)+0$")
    maxLen = 0
    res = '-1'
    for c in num:
        # 如果当前是一个0，并且栈顶也是0，说明栈中可能存储了一个完整信号（也可能不是完整信号）
        # 注意1010不是完整信号，010是不对的，一个完整信号如果不是在开头，那它开始的0前面必是0
        if c == '0':
            if q and q[-1] == '0':

                # 校验完整信号是否为题目要求的，是的话更新结果
                tmp = "".join(q)
                # if reg.match(tmp) and len(tmp) > maxLen: # 正则检查字符串是否符合
                if check(tmp) and len(tmp) > maxLen: # 普通遍历检查
                    maxLen = len(tmp)
                    res = tmp
                
                # 清空栈中的完整信号
                q.clear()
        q.append(c)

    # 注意要校验栈中剩余的
    if q:
        tmp = "".join(q)
        if reg.match(tmp) and len(tmp) > maxLen:
            maxLen = len(tmp)
            res = tmp
    return res

print(solve(num))

# 00101010101100001010010