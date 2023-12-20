import random

def generate_mountain(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def find_peak(mountain):
    rows, cols = len(mountain), len(mountain[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def neighbors(x, y):
        possible_neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(nx, ny) for nx, ny in possible_neighbors if is_valid(nx, ny)]

    current_x, current_y = random.randint(0, rows - 1), random.randint(0, cols - 1)
    print("Current x:", current_x, "Current y:", current_y)
    while True:
        neighbors_list = neighbors(current_x, current_y)
        next_x, next_y = max(neighbors_list, key=lambda pos: mountain[pos[0]][pos[1]])

        if mountain[next_x][next_y] <= mountain[current_x][current_y]:
            return current_x, current_y
        print("Move to", next_x, next_y)
        current_x, current_y = next_x, next_y

rows, cols = 10, 10
mountain = generate_mountain(rows, cols)
peak_x, peak_y = find_peak(mountain)

print("Mountain:")
for row in mountain:
    print(row)

print("\nPeak found at:", peak_x, peak_y)
print("Peak height:", mountain[peak_x][peak_y])