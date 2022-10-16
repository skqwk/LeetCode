[Каждому по компьютеру](https://contest.yandex.ru/contest/29075/problems/C/)

```Python
groupslen, audslen = map(int, input().split())
groups = list(map(int, input().split()))
for i, group in enumerate(groups):
    groups[i] = (group, i)

auds = list(map(int, input().split()))
for i, aud in enumerate(auds):
    auds[i] = (aud, i + 1) 

auds.sort()
groups.sort()

answers = [0] * groupslen
j = 0
count = 0
for i in range(groupslen):
    group, idx = groups[i]
    while j < audslen and group + 1 > auds[j][0]:
        j += 1
    
    if j == audslen:
        break
    answers[idx] = auds[j][1]
    j += 1
    count += 1

print(count)
print(' '.join(map(str, answers)))
```