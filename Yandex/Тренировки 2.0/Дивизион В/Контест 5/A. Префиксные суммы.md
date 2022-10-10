[Префиксные суммы](https://contest.yandex.ru/contest/29075/problems/A/)

```Python
arrlen, amountreqs = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (arrlen + 1)

for i in range(arrlen):
    prefix[i + 1] = prefix[i] + arr[i]

for i in range(amountreqs):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l - 1])
```