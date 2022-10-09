amount = int(input())

count = {}

for i in range(amount):
    color, num = map(int, input().split())
    count[color] = count.get(color, 0) + num

for color in sorted(count.keys()):
    print(color, count[color])