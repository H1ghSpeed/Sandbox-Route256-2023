count = int(input())

for i in range(count):
    ls1 = int(input())
    ls = list(map(int, input().split()))
    suma = sum(ls)
    a = {}
    for j in ls:
        try:
            a[j] += 1
        except:
            a[j] = 1
    for j in a:
        suma -= a[j] // 3 * j
    print(suma)
