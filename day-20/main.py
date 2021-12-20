def enhance_pixel(row, col, image, image_enhancement_algorithm, background):
    output_pixel = [[background for _ in range(3)] for _ in range(3)]
            
    # top
    if row > 0: 
        if col > 0: #top left
            output_pixel[0][0] = image[row-1][col-1]
        
        # top middle
        output_pixel[0][1] = image[row-1][col]

        if col < len(image) - 1: # right edge
            output_pixel[0][2] = image[row-1][col+1]

    # middle
    if col > 0: # middle-left
        output_pixel[1][0] = image[row][col-1]

    output_pixel[1][1] = image[row][col]

    if col < len(image) - 1: # right edge
        output_pixel[1][2] = image[row][col+1]

    # bottom
    if row < len(image) - 1:
        if col > 0: # bottom-left
            output_pixel[2][0] = image[row+1][col-1]

        output_pixel[2][1] = image[row+1][col]

        if col < len(image) - 1: # bottom-right
            output_pixel[2][2] = image[row+1][col+1]

    output_pixel_bin = ''.join(['1' if j == '#' else '0' for sub in output_pixel for j in sub])
    return image_enhancement_algorithm[int(output_pixel_bin, 2)]

def enhance_image(input_image, image_enhancement_algorithm, iterations=1):
    background = '.'

    i = 1
    while i <= iterations:
        
        # should i not be increasing the grid?
        temp = [[background for _ in range(len(input_image)+2)] for _ in range(len(input_image)+2)]
        output_image = [arr.copy() for arr in temp]

        for row in range(1, len(output_image)-1):
            for col in range(1, len(output_image)-1):
                temp[row][col] = input_image[row-1][col-1]

        # enhance image
        for row in range(0, len(output_image)):
            for col in range(0, len(output_image)):
                output_image[row][col] = enhance_pixel(row, col, temp, image_enhancement_algorithm, background)
        
        input_image = output_image

        if image_enhancement_algorithm[0] == '#':  # we need to flip ## HACK ##
            background = '#' if background == '.' else '.'

        i += 1

    return output_image


def print_image(image):
    print('-------------')
    for row in range(0, len(image)):
        for col in range(0, len(image)):
            print(image[row][col], end='')
        print()

with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

    image_enhancement_algorithm = [c for c in lines[0]]

    input_image = []
    for line in lines[2:]:
        input_image.append(line)

    enhanced_image = enhance_image(input_image, image_enhancement_algorithm, 2)
    print("part_one", sum([1 if j == '#' else 0 for sub in enhanced_image for j in sub])) # 5285, 5362

    enhanced_image = enhance_image(input_image, image_enhancement_algorithm, 50)
    print("part_two", sum([1 if j == '#' else 0 for sub in enhanced_image for j in sub])) # 5285, 5362