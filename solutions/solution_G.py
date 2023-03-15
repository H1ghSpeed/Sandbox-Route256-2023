
par, count = map(int, input().split())
friends = {}
for j in range(1, par+1):
    friends[j] = []
for i in range(count):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
for key in friends:
    if len(friends[key]) == 0:
        print(0)
        continue
    elif len(friends[key]) == 1:
        if friends[friends[key][0]] == [key]:
            print(0)
        else:
            for friend in friends[friends[key][0]]:
                if friend == key:
                    continue
                print(friend, end=" ")
            print()
    else:
        res = []
        for friend in friends[key]:
            for id in friends[friend]:
                if not id in friends[key] and id != key:
                    res.append((id, friend))
        print(res)
        if len(res) > 0:
            print(max(set(res), key=res.count))
        else:
            print(0)
print(friends)
