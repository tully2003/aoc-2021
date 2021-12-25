def print_seaworms(map, sea_worms):
    for row in range(0, len(map)):
        for col in range(0, len(map[row])):
            c = '.'
            if (row, col) in sea_worms:
                c = sea_worms[(row,col)]
            print(c, end='')
        print()

with open("input.txt") as file:
    map = [line.strip() for line in file.readlines()]
    sea_worms = {(r,c): map[r][c] for r in range(0, len(map)) for c in range(0, len(map[r])) if map[r][c] in [">", "v"]}

    step = 0
    moving = True
    while moving:
        moves = {}
        moving = False

        # east facing first!
        for position in [pos for (pos,sw) in sea_worms.items() if sw == '>']:
            (row, col) = position

            next_col = col+1 if col+1 < len(map[row]) else 0
            if (row, next_col) not in sea_worms:
                moves[(row, col)] = ((row,next_col), '>')
                moving = True

        for (current, move) in moves.items():
            (row, col), value = move
            sea_worms[(row, col)] = value
            del sea_worms[current]
        moves.clear()

        # now south facing
        for position in [pos for (pos,sw) in sea_worms.items() if sw == 'v']:
            (row, col) = position

            next_row = row+1 if row+1 < len(map) else 0
            if (next_row, col) not in sea_worms:
                moves[(row, col)] = ((next_row,col), 'v')
                moving = True

        for (current, move) in moves.items():
            (row, col), value = move
            sea_worms[(row, col)] = value
            del sea_worms[current]

        step += 1 
        
print("part_one", step)