with open("./inputs/2019_03.txt") as f:
    data = f.read().strip()

a, b = data.split("\n")
a = a.split(",")
b = b.split(",")


def solve(a, b):
    curr = [0, 0]
    aPoints = {}
    translate = {"R": [1, 0], "L": [-1, 0], "D": [0, -1], "U": [0, 1]}
    steps = 0
    for op in a:
        dir = op[0]
        count = int(op[1:])
        for _ in range(count):
            curr = [curr[0] + translate[dir][0], curr[1] + translate[dir][1]]
            steps += 1
            key = str(curr[0]) + ":" + str(curr[1])
            if key not in aPoints:
                aPoints[key] = steps

    curr = [0, 0]
    steps = 0
    bPoints = {}
    for op in b:
        dir = op[0]
        count = int(op[1:])
        for _ in range(count):
            curr = [curr[0] + translate[dir][0], curr[1] + translate[dir][1]]
            steps += 1
            key = str(curr[0]) + ":" + str(curr[1])
            if key not in bPoints:
                bPoints[key] = steps

    res = float("inf")
    for key in aPoints:
        if key in bPoints:
            res = min(res, aPoints[key] + bPoints[key])
    return res


def test():
    a = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
    b = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")
    print(solve(a, b))

    a = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
    b = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")
    print(solve(a, b))


# test()
print(solve(a, b))
