[Максимальная сумма](https://contest.yandex.ru/contest/29075/problems/B/)

Накапливаем сумму и в тот момент, когда она становится отрицательной - сбрасываем и начинаем заново.
```Python
lenarr = int(input())

arr = list(map(int, input().split()))
sum = arr[0]
best = arr[0]
for i in range(1, lenarr):
    sum = max(arr[i], arr[i] + sum)
    best = max(best, sum)

print(best)
```