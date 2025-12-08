import numpy as np
from scipy.cluster.hierarchy import fcluster, single
from scipy.spatial.distance import pdist, squareform

with open("day8/input.txt", "r") as f:
    boxes = f.read().strip().split("\n")

boxes = np.array([j.split(",") for j in boxes], dtype=int)

dists = pdist(boxes, "euclidean")
linkage = single(dists)
# Okay, apparently "nothing happens" means a connection is still used
# I'm too deep into clustering now, use a hack since all dists are unique:
exclusions = np.sum(~np.isin(np.sort(dists)[:1000], linkage[:1000, 2]))
clusters = fcluster(linkage, criterion="maxclust", t=len(boxes) - (1000 - exclusions))
_, counts = np.unique_counts(clusters)
score = np.prod(np.sort(counts)[-3:])
print(score)

last_box_left = int(linkage[-1, 0])
last_box_right = int(np.argsort(squareform(dists)[last_box_left])[1])  # 0 is itself
score2 = boxes[last_box_left, 0] * boxes[last_box_right, 0]
print(score2)
