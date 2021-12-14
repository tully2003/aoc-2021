def parse():
    insertion_rules={}
    with open("input.txt") as file:
        lines = file.readlines()

        template = lines[0].strip()

        for line in lines[2:]:
            key, value = line.strip().split(' -> ')
            insertion_rules[key] = value

        print(insertion_rules)

    return template, insertion_rules

def part_one(template, insertion_rules):
    step = 1
    while step <= 10:
        temp = ''
        #print(template)
        char_counts = {}
        for (idx, c) in enumerate(template):
            temp += c
            if c not in char_counts:
                char_counts[c] = 0
            char_counts[c] += 1

            if idx+1 < len(template):
                ins = insertion_rules[c+template[idx+1]]
                temp += ins

                if ins not in char_counts:
                    char_counts[ins] = 0
                char_counts[ins] += 1

        template = temp
        #print(f"After step {step}: {template}")
        print(char_counts)
        print(step, max(char_counts.values()) - min(char_counts.values()), len(template))
        step += 1


def part_two(template, insertion_rules):
    base_pairs = {k: 0 for k,_ in insertion_rules.items()}
    pairs = dict(base_pairs)

    # create initial pairs
    for i in range(0, len(template)-1):
        pairs[template[i:i+2]] += 1

    step = 1
    while step <= 40:
        temp = dict(base_pairs)

        for pair in pairs:
            temp[pair[0]+insertion_rules[pair]] += pairs[pair]
            temp[insertion_rules[pair] + pair[1]] += pairs[pair]

        pairs = temp
        step += 1

    char_counts = {v: 0 for v in insertion_rules.values()}
    for pair in pairs:
        char_counts[pair[0]] += pairs[pair]
        char_counts[pair[1]] += pairs[pair]
    char_counts[template[0]] += 1
    char_counts[template[-1]] += 1

    print((max(char_counts.values())-min(char_counts.values()))/2)
    

template, insertion_rules = parse()
part_one(template, insertion_rules)
print("---------------------")
part_two(template, insertion_rules)

