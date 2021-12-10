def print_corruption(expected, found, expr):
    print(f"{expr.strip()} - expected {expected}, but found {found} instead")

def calc_autocomplete_score(stack):
    completion_scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    score = 0

    while len(stack) != 0:
        char = stack.pop()
        next_char = ''
        if char == '(':
            next_char = ')'
        elif char == '[':
            next_char = ']'
        elif char == '{':
            next_char = '}'
        elif char == '<':
            next_char = '>'
        
        score = score * 5 + completion_scores[next_char]

    return score

corruption_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


with open("input.txt") as file:
    corruption_score = 0
    autocompletes = []
    for expr in file.readlines():
        stack = []
        corrupt = False
        for char in expr.strip():
            if char in ["(","[","{","<"]:
                stack.append(char)
            else:
                # we need to pop
                current_char = stack.pop()

                if current_char == '(' and char != ')':
                    print_corruption(")", char, expr)
                    corruption_score+=corruption_scores[char]
                    corrupt = True
                    break
                elif current_char == '[' and char != ']':
                    print_corruption("]", char, expr)
                    corruption_score+=corruption_scores[char]
                    corrupt = True
                    break
                elif current_char == '{' and char != '}':
                    print_corruption("}", char, expr)
                    corruption_score+=corruption_scores[char]
                    corrupt = True
                    break
                elif current_char == '<' and char != '>':
                    print_corruption(">", char, expr)
                    corruption_score+=corruption_scores[char]
                    corrupt = True
                    break
            
        if not corrupt:
            xxx = calc_autocomplete_score(stack)
            print(f"{expr.strip()} - {xxx} total points")
            autocompletes.append(xxx) 

    print(corruption_score)

    autocompletes.sort()
    print(autocompletes[int(len(autocompletes)/2)])
