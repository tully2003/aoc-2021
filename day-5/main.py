from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


def part_one():
    with open("input.txt") as file:
        map = {}
        for raw_line in file.readlines():
            line_ = raw_line.split(" -> ")
            start = Point(int(line_[0].split(',')[0]), int(line_[0].split(',')[1].strip()))
            end = Point(int(line_[1].split(',')[0]), int(line_[1].split(',')[1].strip()))

            if start.x == end.x:
                #print(start, end)
                x = start.x

                # if x is the same we have to traverse y!
                y = start.y if start.y < end.y else end.y
                max_y = end.y if start.y < end.y else start.y
                while y <= max_y:
                    current = Point(x, y)
                    #print(current)
                    if current in map:
                        map[current] += 1
                    else:
                        map[current] = 1
                    y += 1
            elif start.y == end.y:
                #print(start, end)
                y = start.y
                
                # if x is the same we have to traverse y!
                x = start.x if start.x < end.x else end.x
                max_x = end.x if start.x < end.x else start.x
                while x <= max_x:
                    current = Point(x, y)
                    #print(current)
                    if current in map:
                        map[current] += 1
                    else:
                        map[current] = 1
                    x += 1
            else:
                continue


        #print(map)

        print(len([n for n in map.values() if n >= 2]))

def part_two():
    with open("input.txt") as file:
        map = {}
        for raw_line in file.readlines():
            line_ = raw_line.split(" -> ")
            start = Point(int(line_[0].split(',')[0]), int(line_[0].split(',')[1].strip()))
            end = Point(int(line_[1].split(',')[0]), int(line_[1].split(',')[1].strip()))

            if start.x == end.x:
                x = start.x

                y = start.y if start.y < end.y else end.y
                max_y = end.y if start.y < end.y else start.y
                while y <= max_y:
                    current = Point(x, y)
                    if current in map:
                        map[current] += 1
                    else:
                        map[current] = 1
                    y += 1
            elif start.y == end.y:
                y = start.y
                
                x = start.x if start.x < end.x else end.x
                max_x = end.x if start.x < end.x else start.x
                while x <= max_x:
                    current = Point(x, y)
                    #print(current)
                    if current in map:
                        map[current] += 1
                    else:
                        map[current] = 1
                    x += 1
            else:
                #must be diagonal
                x = start.x
                y = start.y

                while x != end.x and y != end.y:
                    current = Point(x, y)
                    #print(current)
                    if current in map:
                        map[current] += 1
                    else:
                        map[current] = 1
                    x = x+1 if x < end.x else x-1
                    y = y+1 if y < end.y else y-1

                # hack
                current = Point(x, y)
                if current in map:
                    map[current] += 1
                else:
                    map[current] = 1

        print(len([n for n in map.values() if n >= 2]))


def _print_map(map):
    print(map)
    print('')
    for y in range(10):
        row = ''
        for x in range(10):
            point = Point(x, y)
            if point in map:
                row += str(map[point])
            else:
                row += '.'
        print(row)


part_one()
part_two()