[E. Отбраковка](https://contest.yandex.ru/contest/39714/problems/E)

```Python
def removeVowels(s):
    for vowel in 'aeiou':
        s = s.replace(vowel, ' ')
    return s;

input()
substances = list(input().split())

best = set()
good = {}
norm = {}
for substance in substances:
    best.add(substance)
    if substance.lower() not in good:
        good[substance.lower()] = substance
    if removeVowels(substance.lower()) not in norm:
        norm[removeVowels(substance.lower())] = substance

input()
produced = list(input().split())

ans = []

for substance in produced:
    if substance in best:
        ans.append(substance)
    elif substance.lower() in good:
        ans.append(good[substance.lower()])
    elif removeVowels(substance.lower()) in norm:
        ans.append(norm[removeVowels(substance.lower())])
    else:
        ans.append('')

print(' '.join(ans))

```