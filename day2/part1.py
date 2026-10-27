from pathlib import Path


def get_ranges(text):
    ranges = []
    for part in text.strip().split(","):
        lo, hi = part.split("-")
        ranges.append((int(lo), int(hi)))
    return ranges


def find_invalid_ids(lo, hi):
    # An invalid ID with half-length k is h * (10**k + 1), where h is a k-digit
    # number (e.g. 123 * 1001 = 123123). So instead of scanning every ID in the
    # range, compute which h values land inside [lo, hi].
    for k in range(1, len(str(hi)) // 2 + 1):
        multiplier = 10**k + 1
        h_min = max(10 ** (k - 1), -(-lo // multiplier))
        h_max = min(10**k - 1, hi // multiplier)
        for h in range(h_min, h_max + 1):
            yield h * multiplier


def solve(text):
    return sum(sum(find_invalid_ids(lo, hi)) for lo, hi in get_ranges(text))


print(solve((Path(__file__).parent / "input.txt").read_text()))
