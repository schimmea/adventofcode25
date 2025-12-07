import numpy as np

with open("day6/input.txt", "r") as f:
    data = f.read().strip().split("\n")

ops = data.pop(-1).strip().split()

problems = []
colnums = []
for eles in zip(*data):
    num = "".join(eles).strip()
    if num == "":
        problems.append(colnums)
        colnums = []
        continue
    colnums.append(num)
problems.append(colnums)  # Last iteration

score = 0
for nums, op in zip(problems, ops):
    row = np.array(nums, dtype=int)
    if op == "+":
        score += np.sum(row)
    elif op == "*":
        score += np.prod(row)
print(score)
