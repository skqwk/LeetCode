input()
nums = list(map(int, input().split()))
prefix = [0] * (len(nums) + 1)

for i in range(len(nums)):
    if nums[i] > 0:
        prefix[i + 1] = 1 + prefix[i]
    else:
        prefix[i + 1] = prefix[i]


n = int(input())
answers = []
for i in range(n):
    req = list(map(int, input().split()))
    answers.append(prefix[req[1]] - prefix[req[0] - 1])

for answer in answers:
    print(answer)