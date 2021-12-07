
def part_one(report):
    gamma = ''
    epsilon = ''

    for i in range(12):
        one = 0
        zero = 0
        for line in report:
            if int(line[i]) == 1:
                one += 1
            else:
                zero += 1

        if zero > one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(int(gamma, 2)*int(epsilon, 2))

def part_two(report):
    def filter_arr(arr, i, most_common, high):
        if len(arr) <= 1:
            return arr
        one = []
        zero = []
        for line in arr:

            if int(line[i]) == 1:
                one.append(line)
            else:
                zero.append(line)

        if most_common:
            if high:
                arr = one if len(one) >= len(zero) else zero
            else:
                arr = zero if len(zero) >= len(one) else one
        if not most_common:
            if high:
                arr = one if len(one) <= len(zero) else zero
            else:
                arr = zero if len(zero) <= len(one) else one

        return filter_arr(arr, i+1, most_common, high)

    ogr = filter_arr(report, 0, True, True)[0]
    co2 = filter_arr(report, 0, False, False)[0]

    print(int(ogr, 2) * int(co2, 2))

with open("input.txt") as file:
    report = file.readlines()

    part_one(report)
    part_two(report)