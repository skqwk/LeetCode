[Правильная, круглая, скобочная](https://contest.yandex.ru/contest/29075/problems/D/)

```Python
OPEN = '('
CLOSE = ')'
sequence = input()

count = 0
for par in sequence:
    if par == OPEN:
        count += 1
    elif par == CLOSE:
        count -= 1
        if count < 0:
            break

if (count == 0):
    print('YES')
else:
    print('NO')
```