with open("day4/input.txt") as f:
    grid = [line.strip() for line in f if line.strip()]

rows, cols = len(grid), len(grid[0])
accessible = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "@":
            continue

        # dr = delta row, neighboring cell. nr = neighbor row, row of neighbor cell. 
        neighbors = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    neighbors += 1

        if neighbors < 4:
            accessible += 1

print(accessible)
