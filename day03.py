def parse_data(filename):
    data = open(filename)
    wire1 = data.readline().strip().split(',')
    wire2 = data.readline().strip().split(',')
    data.close()
    return wire1, wire2


def map_wire(grid,wire,value):
    x = 0
    y = 0
    step = 0
    steps = {}
    for path in wire:
        move = int(path[1:])
        for i in range(move):
            if "R" in path:
                x += 1
            if "L" in path:
                x -= 1
            if "D" in path:
                y += 1
            if "U" in path:
                y -= 1
            step += 1
            position = "({},{})".format(x,y)
            steps[position] = step
            if position in grid:
                if grid[position] != value:
                    grid[position] = 5
            else:
                grid.update( {position : value} )
    return grid, steps


def get_intersections(grid):
    intersections = []
    for item in grid.items():
        if int(item[-1]) == 5:
            intersections.append(item[0])
    return intersections


def get_distances(points):
    distances = []
    for item in points:
        a,b = item[1:-1].split(",")
        distances.append(abs(int(a))+abs(int(b)))
    return distances


def get_steps(wire,points):
    step_list = []
    for item in points:
        step_list.append(wire[item])
    #print(step_list)
    return step_list

def find_least_steps(steps1,steps2):
    least_steps = []
    for i in range(len(steps1)):
        least_steps.append(int(steps1[i])+int(steps2[i]))
    return sorted(least_steps)[0]

def main():
    wire1, wire2 = parse_data(r'day03-input.txt')
    grid = {}
    grid, wire1_path = map_wire(grid,wire1,1)
    grid, wire2_path = map_wire(grid,wire2,2)
    intersections = get_intersections(grid)
    distances = get_distances(intersections)
    print("part 1:",sorted(distances)[0])
    steps1 = get_steps(wire1_path,intersections)
    steps2 = get_steps(wire2_path,intersections)
    least_steps = find_least_steps(steps1,steps2)
    print("part 2:",least_steps)


if __name__ == "__main__":
    main()