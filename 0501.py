with open("./inputs/2019_05.txt") as f:
    data = f.read().strip()

data = list(map(lambda x: int(x), data.split(",")))

ADD = 1
MULT = 2
POSITION = 0
IMMEDIATE = 1
INPUT = 3
OUTPUT = 4


def add(data, i, mode1=POSITION, mode2=POSITION, mode3=POSITION):
    a = data[i + 1] if mode1 != POSITION else data[data[i + 1]]
    b = data[i + 2] if mode2 != POSITION else data[data[i + 2]]
    res = a + b
    if mode3 == POSITION:
        data[data[i + 3]] = res
    else:
        data[i + 3] = res


def mult(data, i, mode1=POSITION, mode2=POSITION, mode3=POSITION):
    a = data[i + 1] if mode1 != POSITION else data[data[i + 1]]
    b = data[i + 2] if mode2 != POSITION else data[data[i + 2]]
    res = a * b
    if mode3 == POSITION:
        data[data[i + 3]] = res
    else:
        data[i + 3] = res


def takeInput(data, i, input):
    data[data[i + 1]] = input


def giveOutput(data, i):
    print(data[data[i + 1]])


def transform(data):
    input = 1
    i = 0
    while i < len(data) - 2:
        if data[i] == 99:
            break
        instr = data[i]
        if instr == INPUT:
            takeInput(data, i, input)
            i += 2
        elif instr == OUTPUT:
            giveOutput(data, i)
            i += 2
        elif instr == ADD:
            add(data, i)
            i += 4
        elif instr == MULT:
            mult(data, i)
            i += 4
        else:
            opCode = instr % 100
            instr = instr // 100
            par1 = instr % 10
            instr = instr // 10
            par2 = instr % 10
            instr = instr // 10
            par3 = instr % 10
            instr = instr // 10
            if opCode == ADD:
                add(data, i, par1, par2, par3)
            elif opCode == MULT:
                mult(data, i, par1, par2, par3)
            i += 4


transform(data)
