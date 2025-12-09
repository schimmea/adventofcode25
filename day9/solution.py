import numpy as np
from shapely.geometry import LinearRing, Polygon

with open("day9/input.txt", "r") as f:
    data = f.read().strip().split("\n")

# part 1
coords = np.array([ele.split(",") for ele in data], dtype=int)
diffs = np.abs(coords[:, None, :] - coords[None, :, :])
areas = (diffs + 1).prod(-1)
score1 = np.max(areas)
print(score1)

# part 2
areas[np.tril_indices_from(areas)] = 0
flat_argsort = np.argsort(areas, axis=None)[::-1]
sort_ixs = np.c_[np.unravel_index(flat_argsort, areas.shape)]
sorted_coord_pairs = coords[sort_ixs]
test_rects = np.concatenate(
    [sorted_coord_pairs, sorted_coord_pairs[:, [[0, 1], [1, 0]], [0, 1]]], axis=1
)
tile_poly = Polygon(np.r_[coords, coords[0, None]])
for ixs, test_rect in zip(sort_ixs, test_rects):
    lr = LinearRing(test_rect)
    if tile_poly.contains(lr):
        score2 = areas[*ixs]
        break
print(score2)
