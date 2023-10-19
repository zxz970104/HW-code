n = int(input())
command = []
for i in range(2*n):
    command.append(input())
isSorted = True
size = 0
res = 0
for i in range(0,2*n):
    if i == 0:
        size += 1
        continue
    if "tail add" in command[i]:
        size += 1
    elif "head add" in command[i]:
        size += 1
        isSorted = False
    else:
        size -= 1
        if isSorted:
            continue
        else:
            isSorted = True
            res += 1


print(res)

# 5
# head add 1
# tail add 2
# remove
# head add 3
# tail add 4
# head add 5

# remove
# remove
# remove
# remove