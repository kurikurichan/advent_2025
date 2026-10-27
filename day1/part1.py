
dial = 50
answer = 0

with open("day1/input.txt") as f:
    for line in f:
        line = line.strip()

        dir = line[0]
        ticks = int(line[1:])

        if dir == "R":
            dial = (dial + ticks) % 100
        elif dir == "L":
            dial = (dial - ticks) % 100

        if dial == 0:
            answer += 1

    print(answer)
