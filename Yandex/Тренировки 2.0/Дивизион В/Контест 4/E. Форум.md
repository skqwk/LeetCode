[Форум](https://contest.yandex.ru/contest/28970/problems/E/)

```Python
n = int(input())
topics = {}
messages = {}
for i in range(n):
    num = int(input())
    if num == 0:
        topic = input()
        topics[i + 1] = {'name' : topic, 'amount' : 1}
        messages[i + 1] = i + 1
    else:
        topicnum = messages[num]
        topics[topicnum]['amount'] += 1
        messages[i + 1] = topicnum
    message = input()

maxamount = 0
for topic in topics.values():
    maxamount = max(topic['amount'], maxamount)

for topic in sorted(topics.keys()):
    if topics[topic]['amount'] == maxamount:
        ans = topics[topic]['name']
        break

print(ans)
```
