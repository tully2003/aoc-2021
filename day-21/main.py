from itertools import product

class Pawn:
    def __init__(self, player, starting_position) -> None:
        self.player = player
        self.score = 0
        self.next = None
        self.position = starting_position

def part_one():
    p1 = Pawn(1, 6)
    p2 = Pawn(2, 9)

    p1.next = p2
    p2.next = p1
    deterministic_dice = [i for i in range(1, 101)]
    board = [i for i in range(1,11)]

    current_roll = 0
    current_player = p1

    while p1.score < 1000 and p2.score < 1000:
        # do 3 rolls
        roll_value = deterministic_dice[current_roll%100] + deterministic_dice[(current_roll+1)%100] + deterministic_dice[(current_roll+2)%100]

        new_position = current_player.position + roll_value

        if new_position >= len(board) + 1:
            new_position %= 10
        
        current_player.score += board[new_position-1]
        current_player.position = new_position
        # print(f"Player {current_player.player} rolls {deterministic_dice[current_roll%100]}+{deterministic_dice[(current_roll+1)%100]}+{deterministic_dice[(current_roll+2)%100]} and moves to space {new_position} for a total score of {current_player.score}")

        current_roll += 3
        current_player = current_player.next

    lowest = p1.score if p1.score < p2.score else p2.score
    print("part_one", f"{lowest} * {current_roll} = {lowest*current_roll}")


def part_two():
    possible_rolls = list(product([1,2,3], repeat=3))
    cache = {}

    def dirac_dice(current_player_pos, next_player_pos, current_score, next_score):
        if (current_player_pos, next_player_pos, current_score, next_score) in cache:
            return cache[(current_player_pos, next_player_pos, current_score, next_score)]

        if (current_score >= 21):
            cache[(current_player_pos, next_player_pos, current_score, next_score)] = (1,0)
            return (1, 0)
        if (next_score >= 21):
            cache[(current_player_pos, next_player_pos, current_score, next_score)] = (0,1)
            return (0, 1)

        total_p1_wins = total_p2_wins = 0

        for r1, r2, r3 in possible_rolls:
            new_position = (current_player_pos + r1 + r2 + r3) % 10
            new_score = current_score + new_position + 1

            p2_wins, p1_wins = dirac_dice(next_player_pos, new_position, next_score, new_score)

            total_p1_wins += p1_wins
            total_p2_wins += p2_wins

        cache[(current_player_pos, next_player_pos, current_score, next_score)] = (total_p1_wins, total_p2_wins)
        return (total_p1_wins, total_p2_wins)

    print("part_two", max(dirac_dice(5, 8, 0, 0)))


part_one()
part_two()