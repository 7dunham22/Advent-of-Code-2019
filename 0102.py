with open("./inputs/2019_01.txt") as f:
    data = f.read().strip()

modules = data.split()


def calculate(weight):
    if weight <= 0:
        return weight
    fuelRequired = weight // 3 - 2
    if fuelRequired <= 0:
        return 0
    return fuelRequired + calculate(fuelRequired)


def solve():
    print(sum(map(lambda x: calculate(int(x)), modules)))


def test():
    print("Mass 14: ", calculate(14))
    print("Mass 1969: ", calculate(1969))
    print("Mass 100756: ", calculate(100756))


# test()
solve()
