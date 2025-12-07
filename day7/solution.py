import re
from collections import defaultdict

with open("day7/input.txt", "r") as f:
    data = f.read().strip()

width = data.find("\n")
splitter_cols = [
    res.span()[0] % width for res in re.finditer(r"\^", data.replace("\n", ""))
]
beamcols_merges = defaultdict(int)
beamcols_merges[data.find("S")] = 0
score1, score2 = 0, 1
for sc in splitter_cols:
    if sc not in beamcols_merges:
        continue
    score1 += 1  # part1
    score2 += 1 + beamcols_merges[sc]  # part2
    # Avoid lazy eval shenanigans with defaultdict:
    left_exists = sc - 1 in beamcols_merges
    right_exists = sc + 1 in beamcols_merges
    beamcols_merges[sc - 1] += beamcols_merges[sc] + left_exists
    beamcols_merges[sc + 1] += beamcols_merges[sc] + right_exists
    del beamcols_merges[sc]

print(score1)
print(score2)
