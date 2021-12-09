from itertools import permutations

def part_one():
    with open("input.txt") as file:
        count = 0
        for line in file.readlines():
            output_values = line.split('|')[1].strip().split(' ')
            for value in output_values:
                if len(value) in [2,4,3,7]:
                    count += 1
        print(count)

def part_two():
    segments_permutations = list(permutations(['a','b','c','d','e','f','g']))
    number_patterns = {
        # now see if we can make each digit with this configuration
        0: ['a','b','c','_','e','f','g'],
        1: ['_','_','c','_','_','f','_'],
        2: ['a','_','c','d','e','_','g'],
        3: ['a','_','c','d','_','f','g'],
        4: ['_','b','c','d','_','f','_'],
        5: ['a','b','_','d','_','f','g'],
        6: ['a','b','_','d','e','f','g'],
        7: ['a','_','c','_','_','f','_'],
        8: ['a','b','c','d','e','f','g'],
        9: ['a','b','c','d','_','f','g'],
    }
    
    with open("input.txt") as file:
        output_sum = 0
        for line in file.readlines():
            signal_patterns = line.split('|')[0].strip().split(' ')
            output_values = line.split('|')[1].strip().split(' ')
            signal_patterns.sort(key=len)
            one = [s for s in signal_patterns[0]]
            seven = [s for s in signal_patterns[1] if s not in one]
            four = [s for s in signal_patterns[2] if s not in one]
            
            for option in segments_permutations:
                # short cut to permutations that could work
                if option[2] not in one or option[5] not in one:
                    continue
                if option[0] not in seven:
                    continue
                if option[1] not in four or option[3] not in four:
                    continue

                option_patterns = {k:''.join([option[i] if v[i] != '_' else '' for i,_ in enumerate(v)]) for k, v in number_patterns.items()}
                
                #for each permutation try and match it to the signal
                matched_patterns = {}
                for signal_patten in signal_patterns:
                    for k,v in option_patterns.items():
                        if sorted(v) == sorted(signal_patten):
                            matched_patterns[''.join(sorted(signal_patten))] = k
                
                if len(matched_patterns) == 10:
                    output = ''
                    for value in output_values:
                        output += f"{matched_patterns[''.join(sorted(value))]}"
                    output_sum += int(output)
                    break

        print(output_sum)

part_one()
part_two()