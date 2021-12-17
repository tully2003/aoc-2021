from dataclasses import dataclass

@dataclass
class Velocity:
    x: int
    y: int

@dataclass
class Position:
    x: int
    y: int


with open("input.txt") as file:
    raw_input = file.read()

    x_raw, y_raw = raw_input.replace("target area: ", "").split(', ')
    x_start, x_end = [int(x) for x in x_raw.replace("x=", "").split("..")]
    y_start, y_end = [int(y) for y in y_raw.replace("y=", "").split("..")]

    target = {"x": {"start": x_start,"end": x_end}, "y": {"start": y_start,"end": y_end}}
    successful_velocities = []
    max_height = -100000000000
    for x in range(0, target["x"]["end"]+1):
        for y in range(100, target["y"]["start"]-1, -1):
            initial_velocity = velocity = Velocity(x,y)
            current_max_height = -1

            step = 1
            position = Position(0,0)
            while True:
                # update position
                position = Position(position.x + velocity.x, position.y + velocity.y)
                if position.y > current_max_height:
                    current_max_height = position.y

                # change velocity
                x_v = 0
                if velocity.x != 0:
                    x_v = velocity.x - 1 if velocity.x > 0 else + 1
                velocity = Velocity(x_v, velocity.y - 1)

                # in target area
                if position.x >= x_start and position.x <= x_end:
                    if position.y >= y_start and position.y <= y_end:
                        successful_velocities.append(initial_velocity)
                        #print("Reached Target", initial_velocity)
                        if current_max_height > max_height:
                            max_height = current_max_height
                        break

                # missed target
                if position.x > target["x"]["end"] or position.y < target["y"]["start"]:
                    break

                step += 1

    print("part_one", max_height)
    print("part_two", len(successful_velocities))