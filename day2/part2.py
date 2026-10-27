from pathlib import Path

text = (Path(__file__).parent / "input.txt").read_text()

total = 0
for part in text.strip().split(","):
    lo, hi = map(int, part.split("-"))
    for n in range(lo, hi + 1):
        s = str(n)
        for k in range(1, len(s) // 2 + 1):
            if len(s) % k == 0 and s[:k] * (len(s) // k) == s:
                total += n
                break   # stop after the first match so the ID isn't counted twice

print(total)
