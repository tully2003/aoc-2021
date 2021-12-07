
with open("input.txt") as file:
    h = 0
    d = 0
    aim = 0
    for instruction in file.readlines():
        command = instruction.split(' ')[0]
        value = int(instruction.split(' ')[1])

        if command == "forward":
            h += value
            d += aim * value
        elif command == "up":
            #d -= value
            aim -= value
        elif command == "down":
            #d += value
            aim += value

    print (h*d)

