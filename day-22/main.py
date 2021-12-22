class Cuboid:
    def __init__(self, x, y, z, on=True):
        self.x = x
        self.y = y
        self.z = z
        self.on = on

    def size(self):
        x = self.x[1] - self.x[0] + 1
        y = self.y[1] - self.y[0] + 1
        z = self.z[1] - self.z[0] + 1
        return x * y * z * (-1 if not self.on else 1)

    def __repr__(self):
        return f"{'on' if self.on else 'off'} x={self.x}, y={self.y} z={self.z}"


def parse_command(raw) -> Cuboid:
    return Cuboid(
        x=[int(x) for x in raw.split(' ')[1].split(',')[0].replace('x=', '').split('..')],
        y=[int(y) for y in raw.split(' ')[1].split(',')[1].replace('y=', '').split('..')],
        z=[int(z) for z in raw.split(' ')[1].split(',')[2].replace('z=', '').split('..')],
        on=True if raw.split(' ')[0] == "on" else False
    )

def lineIntersection(a, b):
    left = max(a[0], b[0])
    right = min(a[1], b[1])
    if right - left <= 0:
        return False
    return (left, right)

def intersection(cube1, cube2):
    x = lineIntersection(cube1.x, cube2.x)
    y = lineIntersection(cube1.y, cube2.y)
    z = lineIntersection(cube1.z, cube2.z)
    if x and y and z:
        return Cuboid(x, y, z)
    return False


def part_one(cubes):
    lit_cubes = {}

    for cube in cubes:
        if any([True for x in cube.x if x > 50 or x < -50]):
            continue 

        for x in range(cube.x[0], cube.x[1]+1):
            for y in range(cube.y[0], cube.y[1]+1):
                for z in range(cube.z[0], cube.z[1]+1):
                    lit_cubes[(x,y,z)] = cube.on == 1
                    
    print("part_one", len([c for c in lit_cubes.values() if c]))


def part_two(cubes):
    # Add the cubes together and subtract the intersections, making sure that nothing is counted more than it's necessary.
    all_cubes = [cubes[0]]

    for cube in cubes[1:]:
        for existing_cube in all_cubes.copy():
            intersect_cube = intersection(cube, existing_cube)

            if intersect_cube:
                if existing_cube.on:
                    intersect_cube.on = False
                all_cubes.append(intersect_cube)
        if cube.on:
            all_cubes.append(cube)

    print("part_two", sum([cube.size() for cube in all_cubes])) # 1284561759639324


with open('input.txt') as file:
    cubes = [parse_command(line.strip()) for line in file.readlines()]
    
    part_one(cubes)
    part_two(cubes)