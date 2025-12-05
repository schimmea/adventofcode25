import numpy as np

with open("day5/input.txt", "r") as f:
    ranges, ids = f.read().strip().split("\n\n")

ranges = np.array([r.split("-") for r in ranges.split("\n")], dtype=int)
ids = np.array(ids.split("\n"), dtype=int)

lower_bound = ids[:, None] >= ranges[:, 0]
upper_bound = ids[:, None] <= ranges[:, 1]
score = np.logical_and(lower_bound, upper_bound).any(1).sum()
print(score)
