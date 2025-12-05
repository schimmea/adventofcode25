import numpy as np


def deoverlap(arr: np.ndarray):
    # I'm sure this works without recursion, but it's fast enough
    new_arr = arr.copy()
    below_lower_bounds = new_arr[:, 0, None] <= new_arr[:, 0]
    above_lower_bounds = new_arr[:, 1, None] >= new_arr[:, 0]
    encapsulates = np.logical_and(below_lower_bounds, above_lower_bounds)
    encapsulates[np.diag_indices_from(encapsulates)] = 0
    if not encapsulates.any():
        return new_arr
    encapsulate_indices = np.stack(np.where(encapsulates), axis=1)
    for eix in encapsulate_indices:
        new_arr[eix] = [
            min(new_arr[eix, 0]),
            max(new_arr[eix, 1]),
        ]
    return deoverlap(np.unique(new_arr, axis=0))


with open("day5/input.txt", "r") as f:
    ranges, _ = f.read().strip().split("\n\n")

ranges = np.array([r.split("-") for r in ranges.split("\n")], dtype=int)
deoverlapped_ranges = deoverlap(ranges)

score = np.sum(deoverlapped_ranges[:, 1] - deoverlapped_ranges[:, 0] + 1)
print(score)
