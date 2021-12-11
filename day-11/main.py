def print_octopuses(octopuses, step):
    if step == 0:
        print("Before any steps:")
    else:
        print(f"After step {step}:")

    for row in octopuses:
        #print(row)
        print(''.join([str(i) for i in row]))

def update_neighbours(octopuses, row, col):
    # do neighbours above
    if row > 0:
        octopuses[row-1][col] += 1

        if col > 0:
            octopuses[row-1][col-1] += 1

        # go right
        if col < len(octopuses[row])-1:
            octopuses[row-1][col+1] += 1

    # do left neighbour
    if col > 0:
        octopuses[row][col-1] += 1

    # do right neighbour
    if col < len(octopuses[row])-1:
        octopuses[row][col+1] += 1

    # do neighbours below
    if row < len(octopuses[row])-1:
        octopuses[row+1][col] += 1

        if col > 0:
            octopuses[row+1][col-1] += 1

        # go right
        if col < len(octopuses[row])-1:
            octopuses[row+1][col+1] += 1

def part_one(octopuses):
    total_flash_count = dumbo_octopus(octopuses, 100)
    print(total_flash_count)

def part_two(octopuses):
    dumbo_octopus(octopuses, stop_when_all_zero=True)

def dumbo_octopus(octopuses, max_steps=10000, stop_when_all_zero=False):
    total_flash_count = 0
    step = 0
    #print_octopuses(octopuses, step)
    while(step < max_steps):
        flash_count = 0
        # first pass increment everything by 1
        for row, _ in enumerate(octopuses):
            for col, _ in enumerate(octopuses[row]):
                octopuses[row][col] += 1

        # now produces flashes
        produce_flashes = True
        flashed = {}
        while(produce_flashes):
            produce_flashes = False
            
            for row, _ in enumerate(octopuses):
                for col, _ in  enumerate(octopuses[row]):
                    if octopuses[row][col] > 9:

                        if (row, col) in flashed:
                            continue

                        flash_count += 1
                        flashed[(row, col)] = True
                        produce_flashes = True
                        update_neighbours(octopuses, row, col)

        # final pass reset > 9 to zero
        for row, _ in enumerate(octopuses):
            for col, _ in  enumerate(octopuses[row]):
                if octopuses[row][col] > 9:
                    octopuses[row][col] = 0

        step += 1
        total_flash_count+=flash_count

        if stop_when_all_zero and len(flashed) == 100:
            print_octopuses(octopuses, step)
            break

        #print_octopuses(octopuses, step)
    return total_flash_count



with open("input.txt") as file:
    octopuses = [] 
    for line in file.readlines():
        octopuses.append([int(o) for o in line.strip()])

    part_one([o.copy() for o in octopuses])
    part_two([o.copy() for o in octopuses])
