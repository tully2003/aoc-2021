def part_one(draw_numbers, boards):
    for num in draw_numbers:
        for board in boards:
            # mark numbers
            for _, row in enumerate(board):
                # check if row is done
                for col, value in enumerate(row):
                    if value == num:
                        row[col]= -1

            # check win
            win = False
            for _, row in enumerate(board):
                if all([True if col == -1 else False for col in row]):
                    win = True

            if not win:
                for col in range(5):
                    col_win = True
                    for row in range(5):
                        if board[row][col] != -1:
                            col_win = False
                            break
                    if col_win:
                        win = True
                        break

            if win:
                unmarked_numbers_sum = sum([col for row in board for col in row if col != -1])
                print(f"{unmarked_numbers_sum}*{num}")
                print(unmarked_numbers_sum*num)
                return


def part_two(draw_numbers, boards):
    for num in draw_numbers:
        boards_to_remove = []
        
        for board in boards:
            # mark numbers
            for _, row in enumerate(board):
                # check if row is done
                for col, value in enumerate(row):
                    if value == num:
                        row[col]= -1

            # check win
            win = False
            for _, row in enumerate(board):
                if all([True if col == -1 else False for col in row]):
                    win = True

            if not win:
                for col in range(5):
                    col_win = True
                    for row in range(5):
                        if board[row][col] != -1:
                            col_win = False
                            break
                    if col_win:
                        win = True
                        break

            if win:
                if len(boards) == 1:
                    unmarked_numbers_sum = sum([col for row in board for col in row if col != -1])
                    print(f"{unmarked_numbers_sum}*{num}")
                    print(unmarked_numbers_sum*num)
                    return
                    
                boards_to_remove.append(board)
        
        boards = [b for b in boards if b not in boards_to_remove]


with open("input.txt") as file:
    lines = file.readlines()

    draw_numbers = [int(n) for n in lines[0].split(',')]

    current = 2
    boards = []
    while current + 4 < len(lines):
        current_board = []
        for line in lines[current:current+5]:
            current_board.append([int(n) for n in line.split(' ') if n != ''])
        boards.append(current_board)
        current += 6

    part_one(draw_numbers, boards)
    part_two(draw_numbers, boards)