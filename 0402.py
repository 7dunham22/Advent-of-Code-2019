with open("./inputs/2019_04.txt") as f:
    data = f.read().strip()

MIN, MAX = data.split("-")
MIN = int(MIN)
MAX = int(MAX)


def isValid(num):
    prev = None
    hasPair = False
    pairLength = 0
    while num > 0:
        curr = num % 10
        num = num // 10
        if prev != None:
            if curr > prev:
                return False
            elif curr == prev:
                pairLength += 1
            else:
                if pairLength == 2:
                    hasPair = True
                pairLength = 1
        else:
            pairLength += 1
        prev = curr
    return hasPair or pairLength == 2


res = 0
for num in range(MIN, MAX):
    res += isValid(num)

print(res)

# print(isValid(112233))
# print(isValid(123444))
# print(isValid(111122))
