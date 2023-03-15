def validate(start, stop):
    if start[0] > 23 or stop[0] > 23 or start[0] < 0 or stop[0] < 0:
        return "NO"
    elif start[1] > 59 or stop[1] > 59 or start[1] < 0 or stop[1] < 0:
        return "NO"
    elif start[2] > 59 or stop[2] > 59 or start[2] < 0 or stop[2] < 0:
        return "NO"
    start = (start[0]*3600) + (start[1]*60) + start[2]
    stop = (stop[0]*3600) + (stop[1]*60) + stop[2]
    if (start < 0 or start > 86399) or (stop < 0 or stop > 86399):
        return "NO"
    if start > stop:
        return "NO"
    return start, stop


count = int(input())

for i in range(count):
    count_two = int(input())
    l1 = []
    flag = True
    for j in range(count_two):
        start, stop = input().split("-")
        start, stop = start.split(":"), stop.split(":")
        start, stop = [int(x) for x in start], [int(x) for x in stop]
        res_valid = validate(start, stop)
        if res_valid == "NO":
            flag = False
        else:
            l1.append((res_valid[0], -1))
            l1.append((res_valid[1], 1))
    l1.sort()
    online = 0
    for event in l1:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        if online > 1:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
