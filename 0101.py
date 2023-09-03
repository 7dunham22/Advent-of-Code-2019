with open("./inputs/2019_01.txt") as f:
    data = f.read().strip()

modules = data.split()

res = sum(map(lambda x: int(x) // 3 - 2, modules))

print(res)
