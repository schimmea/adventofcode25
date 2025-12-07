import re
from collections import defaultdict

with open("day7/input.txt", "r") as f:
    data = f.read().strip()

width = data.find("\n")
splitter_cols = [
    res.span()[0] % width for res in re.finditer(r"\^", data.replace("\n", ""))
]
beamcols_timelines = defaultdict(int)
beamcols_timelines[data.find("S")] = 1
splits = 0
for sc in splitter_cols:
    if sc not in beamcols_timelines:
        continue
    splits += 1
    beamcols_timelines[sc - 1] += beamcols_timelines[sc]
    beamcols_timelines[sc + 1] += beamcols_timelines[sc]
    del beamcols_timelines[sc]

print(splits)  # part 1
print(sum(beamcols_timelines.values()))  # part 2
