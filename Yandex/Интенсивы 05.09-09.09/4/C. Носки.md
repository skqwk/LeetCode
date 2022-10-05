[C. Носки](https://contest.yandex.ru/contest/40183/problems/C/)

```Python
length, socks, checks = list(map(int, input().split()))

START = -1
CHECK = 0
END = 1

points = []
for i in range(socks):
    s, e = list(map(int, input().split()))
    points.append((s, START))
    points.append((e, END))

order = []
for i in range(checks):
    pos  = int(input())
    order.append(pos)
    points.append((pos, CHECK))

points.sort()

layers = 0
ans = {}
for point in points:
    if point[1] == START:
        layers += 1
    elif point[1] == END:
        layers -= 1
    else:
        ans[point[0]] = layers

for i in order:
    print(ans[i])
```

