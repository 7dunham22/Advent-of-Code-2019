with open("./inputs/2019_02.txt") as f:
    data = f.read().strip()

data = list(map(lambda x: int(x), data.split(",")))

target = 19690720


def calculate(data, i=0):
    if i >= len(data) - 4 or data[i] == 99:
        return data[0] == target
    if data[i] == 1:
        conversion = data[data[i + 1]] + data[data[i + 2]]
    else:
        conversion = data[data[i + 1]] * data[data[i + 2]]
    data[data[i + 3]] = conversion
    res = calculate(data, i + 4)
    return res


def solve():
    for l in range(100):
        for r in range(100):
            copy = data[:]
            copy[1] = l
            copy[2] = r
            if calculate(copy):
                return 100 * copy[1] + copy[2]
    return "There's been a problem"


print(solve())
