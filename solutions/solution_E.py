count = int(input())

for i in range(count):
    amount = int(input())
    list_first = list(map(int, input().split()))
    dict_verif = {}
    flag = True
    if amount == len(set(list_first)):
        pass
    else:
        for num, item in enumerate(list_first):
            try:
                dict_verif[item] += 1
            except:
                dict_verif[item] = 1
            if dict_verif[item] > 1:
                if list_first[num-1] != item:
                    flag = False
                    break
    if flag:
        print("YES")
    else:
        print("NO")
