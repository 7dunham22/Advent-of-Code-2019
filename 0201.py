with open("./inputs/2019_02.txt") as f:
    data = f.read().strip()

data = list(map(lambda x: int(x), data.split(",")))


def transform(data):
    i = 0
    while i < len(data) - 4:
        if data[i] == 99:
            break
        conversion = None
        if data[i] == 1:
            conversion = data[data[i + 1]] + data[data[i + 2]]
        else:
            conversion = data[data[i + 1]] * data[data[i + 2]]
        data[data[i + 3]] = conversion
        i += 4
    return data


def solve():
    data[1] = 12
    data[2] = 2
    print(transform(data))


def test():
    print(transform([1, 0, 0, 0, 99]))
    print(transform([2, 3, 0, 3, 99]))
    print(transform([2, 4, 4, 5, 99, 0]))
    print(transform([1, 1, 1, 4, 99, 5, 6, 0, 99]))


# test()
solve()
