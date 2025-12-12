import numpy as np

with open("day12/input.txt", "r") as f:
    *presents, spaces = f.read().strip().split("\n\n")

presents = (
    np.array([[*map(list, present.split("\n")[1:])] for present in presents]) == "#"
)
spaces, targets = zip(*[ele.split(": ") for ele in spaces.split("\n")])
spaces = [np.zeros(tuple(map(int, space.split("x")[::-1]))) for space in spaces]
targets = [np.array(target.split(), dtype=int) for target in targets]

score = 0
for space, target in zip(spaces, targets):
    presents_to_fit = np.repeat(presents, target, axis=0)

    # Don't hate the solution, hate the problem
    if presents_to_fit.sum(None) <= np.prod(space.shape):
        score += 1
print(score)
