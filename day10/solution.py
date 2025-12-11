import re
from typing import List

import numpy as np
from scipy.optimize import linprog


def densify(sparse_mat: List[np.ndarray]) -> np.ndarray:
    """Turn button indices to dense bool matrix."""
    ncols = max(map(max, sparse_mat)) + 1
    dense_mat = np.zeros(shape=(len(sparse_mat), ncols), dtype=bool)
    for i, row in enumerate(sparse_mat):
        dense_mat[i, row] = 1
    return dense_mat


with open("day10/input.txt", "r") as f:
    data = f.read().strip()

all_lights = [np.array(list(lights)) == "#" for lights in re.findall(r"\[(.+)\]", data)]
all_buttons = [
    densify(
        [
            np.array(buttons.split(","), dtype=int)
            for buttons in re.findall(r"\((.+?)\)", row)
        ]
    )
    for row in data.split("\n")
]
all_joltages = [
    np.array(joltages.split(","), dtype=int) for joltages in re.findall(r"{(.+)}", data)
]

indicator_scores = []
joltage_scores = []
for lights, joltages, buttons in zip(all_lights, all_joltages, all_buttons):
    # Do breadth-first search for lights
    # Could do it properly with pruning and all but it's fast enough
    indicator_tree = np.zeros_like(lights, dtype=bool)
    i = 0
    while not np.equal(lights, indicator_tree).all(-1).any():
        indicator_tree = indicator_tree ^ buttons[:, *[None] * i]
        i += 1
    indicator_scores.append(i)
    # Do Integer Linear Programming for joltages
    linprog_res = linprog(
        c=np.ones(len(buttons)), A_eq=buttons.T, b_eq=joltages, integrality=1
    )
    j = int(linprog_res.x.sum())
    joltage_scores.append(j)
print(sum(indicator_scores))
print(sum(joltage_scores))
