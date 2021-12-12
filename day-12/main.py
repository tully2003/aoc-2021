class Cave:
    def __init__(self, value: str):
        self.value = value
        self.adjacent = []
        if self.value in ["start", "end"]:
            self._size = "N/A"
        else:
            self._size = "BIG" if self.value.isupper() else "SMALL"

    @property
    def is_small(self):
        return self._size == "SMALL"

    def __repr__(self):
        return f"{self.value} - {self._size} - {','.join([a.value for a in self.adjacent])}"

def build_caves():
    with open("input.txt") as file:
        caves = {}
        for line in file.readlines():
            start = line.split('-')[0
            ].strip()
            end = line.split('-')[1].strip()
            
            if start not in caves:
                caves[start] = Cave(start)

            if end not in caves:
                caves[end] = Cave(end)

            caves[start].adjacent.append(caves[end])
            caves[end].adjacent.append(caves[start])
        return caves

def part_one(caves):
    def count_paths(caves, visited, current):
        path_count = 0
        current_cave = current[len(current)-1]
           
        if current_cave.value == "end":
            #print('->'.join([c.value for c in current]))
            return 1

        if current_cave.is_small or current_cave.value == "start":
            visited[current_cave] = True

        for cave in current_cave.adjacent:
            if cave not in visited:
                current.append(cave)
                path_count += count_paths(caves, visited, current)
                current.pop()

        if current_cave.is_small:
            del visited[current_cave]

        return path_count

    paths = count_paths(caves, {}, [caves["start"]])
    print(paths)

def part_two(caves):
    def count_paths(caves, visited, current):
        path_count = 0
        current_cave = current[len(current)-1]
           
        if current_cave.value == "end":
            #print(','.join([c.value for c in current]))
            return 1

        if current_cave.value == "start":
            visited[current_cave] = -1

        if current_cave.is_small:
            if current_cave not in visited:
                visited[current_cave] = 0

            visited[current_cave] += 1

        for cave in current_cave.adjacent:
            if (cave not in visited or 
               (cave in visited and cave.value != "start" and (visited[cave] == 0 or len([v for (k,v) in visited.items() if k.value != "start" and v > 1]) < 1))):
                current.append(cave)
                path_count += count_paths(caves, visited, current)
                current.pop()

        if current_cave.is_small and current_cave in visited:
            visited[current_cave] -= 1

        return path_count

    paths = count_paths(caves, {}, [caves["start"]])
    print(paths)

part_one(build_caves())
part_two(build_caves())