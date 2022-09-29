input()
ages = list(map(int, input().split()))
ages.sort()
count = 0
for p1 in range(len(ages)):
    p2 = p1 + 1
    while (p2 < len(ages) and ages[p1] > (0.5 * ages[p2] + 7)):
        count += 1
        if ages[p1] == ages[p2]: 
            count += 1
        p2 += 1
print(count)