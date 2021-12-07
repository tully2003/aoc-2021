def part_one():
    calc_lanternfish(80)
    

def part_two():
    calc_lanternfish(256)

def calc_lanternfish(num_lanternfish):
    with open("input.txt") as file:
        lanternfish = [int(f) for f in file.readline().split(',')]
        #print (lanternfish)

        map = {}
        for f in lanternfish:
            if f in map:
                map[f] += 1
            else:
                map[f] = 1

        for day in range(num_lanternfish):
            new_map = {i: 0 for i in range(9)}
            #print(day, map, sum(map.values()))
            for timer in range(9):
                if timer in map:
                    if timer == 0:
                        new_map[6] = map.get(timer, 0)
                        new_map[8] = map.get(timer, 0)
                    elif timer == 7:
                        new_map[6] += map.get(timer, 0)
                    else:
                        new_map[timer-1] = map.get(timer, 0)
            map = new_map

        print(sum(map.values()))

part_one()
part_two()

