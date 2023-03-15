count = int(input())

for i in range(count):
    count_ych = int(input())
    ych = list(map(int, input().split()))
    new_list = []
    for j in range(len(ych)):
        if not j in new_list:
            new_list.append(j)
        else:
            continue
        min = 101
        for k in range(j+1, len(ych)):
            if min > abs(ych[j]-ych[k]) and not k in new_list:
                min = abs(ych[j]-ych[k])
                index = k
        if not index in new_list:
            new_list.append(index)
    for num, x in enumerate(new_list):
        if num % 2 == 0 and num > 0:
            print()
        print(x+1, end=' ')
    print()
