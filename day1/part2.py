class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def build_dial(size=100):
    nodes = [Node(i) for i in range(size)]
    for i, node in enumerate(nodes):
        node.next = nodes[(i + 1) % size]
        node.prev = nodes[(i - 1) % size]
    return nodes


nodes = build_dial()
dial = nodes[50]
answer = 0

with open("day1/input.txt") as f:
    for line in f:
        line = line.strip()

        dir = line[0]
        ticks = int(line[1:])

        for i in range(ticks):
            if dir == "R":
                dial = dial.next
            elif dir == "L":
                dial = dial.prev
            if dial.value == 0:
                answer += 1

    print(answer)
