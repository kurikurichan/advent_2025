total_joltage = 0

with open("day3/input.txt") as f:
    for line in f:
        battery = line.strip()
        if not battery:
            continue

        first = max(battery[:-1])
        i = battery.index(first)

        second = max(battery[i + 1:])

        total_joltage += int(first + second)

    print(total_joltage)
