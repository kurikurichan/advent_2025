with open("day4/input.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]  # lists so cells can be changed

rows, cols = len(grid), len(grid[0])


def count_neighbors(r, c):
    neighbors = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                neighbors += 1
    return neighbors


total_removed = 0

while True:
    # find every accessible roll in this round, then remove them all at once
    to_remove = [
        (r, c)
        for r in range(rows)
        for c in range(cols)
        if grid[r][c] == "@" and count_neighbors(r, c) < 4
    ]
    if not to_remove:
        break

    for r, c in to_remove:
        grid[r][c] = "."
    total_removed += len(to_remove)

print(total_removed)
