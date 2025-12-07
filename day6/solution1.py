import numpy as np

with open("day6/input.txt", "r") as f:
    data = f.read().strip().split("\n")

ops = data.pop(-1).strip().split()
nums = np.array([ele.strip().split() for ele in data], dtype=int)

score = 0
for row, op in zip(nums.T, ops):
    if op == "+":
        score += np.sum(row)
    elif op == "*":
        score += np.prod(row)
print(score)
