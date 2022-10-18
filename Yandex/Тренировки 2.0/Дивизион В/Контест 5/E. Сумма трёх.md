[Сумма трех](https://contest.yandex.ru/contest/29075/problems/E/) 

```Python
s = int(input())

a = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]
c = list(map(int, input().split()))[1:]


mem = {}
for k in range(len(c)):
    if not c[k] in mem:
        mem[c[k]] = k

ans = -1

found = False

for i in range(len(a)):
    for j in range(len(b)):
        partsum = s - (a[i] + b[j])
        if partsum in mem:
            k = mem[partsum]
            ans = i, j, k
            found = True
            break
    if found:
        break

if ans != -1:
    print(*ans)
else:
    print(-1)
```