def part_one(arr):
    low_points = []
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            current = arr[row][col]
            # checkup
            if row > 0:
                if current >= arr[row-1][col]:
                    continue
            
            # check down
            if row < len(arr)-1:
                if current >= arr[row+1][col]:
                    continue

            # check left
            if col > 0:
                if current >= arr[row][col-1]:
                    continue

            # check right
            if col < len(arr[row])-1:
                if current >= arr[row][col+1]:
                    continue

            low_points.append(current)
    
    risk_levels = [value + 1 for value in low_points]
    print(sum(risk_levels))

def part_two(arr):
    # to build a basin you have to from your current position to your lowest point. 
    # alternatively go from your low point until

     # you should build each basin in turn...
     # so start top left and create the basin until you reach the edges?
    low_points = {}
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            current = arr[row][col]
            # checkup
            if row > 0:
                if current >= arr[row-1][col]:
                    continue
            
            # check down
            if row < len(arr)-1:
                if current >= arr[row+1][col]:
                    continue

            # check left
            if col > 0:
                if current >= arr[row][col-1]:
                    continue

            # check right
            if col < len(arr[row])-1:
                if current >= arr[row][col+1]:
                    continue

            if current not in low_points:
                low_points[current] = []
            low_points[current].append((row, col))
    
    # build basins
    basins = []
    for low_point in low_points.values():
        for row, col in low_point:
            basins.append(navigate_basin(arr, row, col, {}))
    basins.sort(reverse=True)
    print([b for b in basins[:3]])
    print(basins[0] * basins[1] * basins[2])

def navigate_basin(arr, row, col, visited):
    # we've been here before
    if (row, col) in visited:
        return 0

    visited[(row,col)] = True

    # we're at a 9 so move on
    if arr[row][col] == 9:
        return 0

    count = 1
    # check up
    if row > 0:
        count += navigate_basin(arr, row-1, col, visited)
    
    # check down
    if row < len(arr)-1:
        count += navigate_basin(arr, row+1, col, visited)

    # check left
    if col > 0:
        count += navigate_basin(arr, row, col-1, visited)

    # check right
    if col < len(arr[row])-1:
        count += navigate_basin(arr, row, col+1, visited)

    return count


with open("input.test.txt") as file:
    arr = [[int(s) for s in line.strip()] for line in file.readlines()]

    part_one(arr)
    part_two(arr)