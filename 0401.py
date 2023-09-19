with open("./inputs/2019_04.txt") as f:
    data = f.read().strip()

MIN, MAX = data.split("-")
MIN = int(MIN)
MAX = int(MAX)


def isValid(num):
    prev = None
    pair = 0
    while num > 0:
        curr = num % 10
        num = num // 10
        if prev != None:
            if curr > prev:
                return False
            elif curr == prev:
                pair += 1
        prev = curr
    return pair > 0


res = 0
for num in range(MIN, MAX):
    res += isValid(num)

print(res)
