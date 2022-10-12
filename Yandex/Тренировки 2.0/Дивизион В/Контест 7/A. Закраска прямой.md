[Закраска прямой](https://contest.yandex.ru/contest/29396/problems/A)

```Python
LEFT = -1
RIGHT = 1

n = int(input())


cuts = []
for i in range(n):
    l, r = map(int, input().split())
    cuts.append([l, r])

cuts.sort()

filled = 0
for i in range(n - 1):
    if cuts[i][1] >= cuts[i + 1][0]:
        cuts[i + 1] = [cuts[i][0], max(cuts[i + 1][1], cuts[i][1])]
    else:
        filled += cuts[i][1] - cuts[i][0]

filled += cuts[n - 1][1] - cuts[n - 1][0]
print(filled)
```