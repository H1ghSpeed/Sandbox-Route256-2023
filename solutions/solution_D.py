count = int(input())

for i in range(count):
    _ = input()
    n, m = map(int, input().split())
    lst_default = []
    for j in range(n):
        lst_default.append(list(map(int, input().split())))
    _ = int(input())
    stolb_sort = list(map(int, input().split()))
    for j in stolb_sort:
        for k in range(n-1):
            for y in range(n-1):
                if lst_default[y][j-1] > lst_default[y+1][j-1]:
                    lst_default[y], lst_default[y +
                                                1] = lst_default[y+1], lst_default[y]
    for i in range(len(lst_default)):
        print(*lst_default[i])
    print()
