total_joltage = 0

with open("day3/input.txt") as f:
    for line in f:
        battery = line.strip()
        if not battery:
            continue

        current_joltage = ""
        last_index = 0

        for i in range(12, 0, -1):
            biggest_num = max(battery[last_index:len(battery) - i + 1])
            last_index = battery.index(biggest_num, last_index) + 1

            current_joltage += biggest_num

        total_joltage += int(current_joltage)

    print(total_joltage)
