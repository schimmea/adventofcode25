from typing import List

with open("day4/input.txt", "r") as f:
    grid = [list(row) for row in f.read().strip().split("\n")]


def get_tp(grid: List[List[str]], remove=False):
    score = 0
    removables = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num_rolls = 0
            if grid[i][j] == ".":
                continue
            if i > 0:
                num_rolls += grid[i - 1][max(0, j - 1) : j + 2].count("@")
            if i < len(grid) - 1:
                num_rolls += grid[i + 1][max(0, j - 1) : j + 2].count("@")
            if j > 0:
                num_rolls += grid[i][j - 1] == "@"
            if j < len(grid[i]) - 1:
                num_rolls += grid[i][j + 1] == "@"
            if num_rolls < 4:
                score += 1
                removables.append((i, j))
    if remove:
        for i, j in removables:
            grid[i][j] = "."
    return score


# part 1:
score1 = get_tp(grid)
print(f"{score1=}")

# part 2:
score2 = 0
while True:
    new_score2 = get_tp(grid, remove=True)
    if new_score2 == 0:
        break
    score2 += new_score2
print(f"{score2=}")
