def part_one(arr):
    increases = sum([1 for i,v in enumerate(arr) if v > arr[i-1]])
    print(increases)

def part_two(arr):
    increases = sum([1 for i in range(3, len(arr)) if arr[i] > arr[i-3]])
    print(increases)


with open("input.txt") as file:
    arr = [int(x) for x in file.readlines()]
    
    part_one(arr)
    part_two(arr)

