with open("input.txt") as file:
    dots = {}
    fold_instructions = []

    read_dots = True
    for line in file.readlines():
        if line.strip() == '':
            read_dots=False
            continue
        if read_dots:
            x, y = line.strip().split(',')
            dots[(int(x),int(y))] = '#'
        else:
            dir, value = line.strip().replace("fold along ", "").split('=')
            fold_instructions.append((dir, int(value)))

    for dir, value in fold_instructions:
        print(f"{dir}={value}")
        if dir == 'y':
            # fold up
            new_dots = {}
            for dot,_ in dots.items():
                x,y = dot
                # above the fold so ignore!
                if y < value:
                    new_dots[(x,y)] = '#'
                    continue

                new_y = value - (y - value)
                if (x, new_y) not in new_dots:
                    new_dots[x, new_y] = '#'

            dots = new_dots
            # print(dots)
            print(len(dots))
        elif dir == 'x':
            # fold left
            new_dots = {}
            for dot,_ in dots.items():
                x,y = dot
                # above the fold so ignore!
                if x < value:
                    new_dots[(x,y)] = '#'
                    continue

                new_x = value - (x - value)
                if (new_x, y) not in new_dots:
                    new_dots[new_x, y] = '#'

            dots = new_dots
            print(len(dots)) # part_one
        else:
            raise Exception(f"UNKNOWN fold direction: {dir}")
    
    # part_two
    for y in range(6):
        for x in range(40):
            print('#' if (x,y) in dots else '.', end='')
        print()
