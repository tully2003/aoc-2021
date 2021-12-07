def part_one(subs):
    map = {}
    max = -1
    min = 10000000000000
    for position in subs:
        if position not in map:
            map[position] = 0
        map[position] += 1

        min = position if position < min else min
        max = position if position > max else max

    # print(min, max, map)
    print(min, max)

    min_fuel = 10000000000000
    max_fuel = -1
    for i in range(min, max+1):
        fuel_cost = sum([abs(pos - i) * count for (pos, count) in map.items()])
        min_fuel = fuel_cost if fuel_cost < min_fuel else min_fuel
        max_fuel = fuel_cost if fuel_cost > max_fuel else max_fuel

    print(min_fuel, max_fuel)


def part_two(subs):
    calculated = {}
    def calc_distance(current, dest):
        if abs(current - dest) in calculated:
            return calculated[abs(current - dest)]

        current_cost = 1
        total_cost = 0
        start = current if current < dest else dest
        end = current if current > dest else dest

        while start < end:
            total_cost += current_cost
            current_cost += 1
            start += 1
        
        calculated[abs(current - dest)] = total_cost
        return total_cost

    map = {}
    max = -1
    min = 10000000000000
    for position in subs:
        if position not in map:
            map[position] = 0
        map[position] += 1

        min = position if position < min else min
        max = position if position > max else max

    # print(min, max, map)
    print(min, max)

    min_fuel = 10000000000000
    max_fuel = -1
    for i in range(min, max+1):
        fuel_cost = sum([calc_distance(pos, i) * count for (pos, count) in map.items()])
        min_fuel = fuel_cost if fuel_cost < min_fuel else min_fuel
        max_fuel = fuel_cost if fuel_cost > max_fuel else max_fuel

    print(min_fuel, max_fuel)


with open("input.txt") as file:
    subs = [int(f) for f in file.readline().split(',')]

    part_one(subs)
    part_two(subs)