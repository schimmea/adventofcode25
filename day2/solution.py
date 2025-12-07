import re

with open("day2/input.txt", "r") as f:
    id_ranges = f.read().strip().split(",")

# part 1:
rex1 = re.compile(r"^(\d+)\1$")
# part 2:
rex2 = re.compile(r"^(\d+)\1+$")

score1, score2 = 0, 0
for idrange in id_ranges:
    start, end = [int(x) for x in idrange.split("-")]
    for id in map(str, range(start, end + 1)):
        if rex1.match(id):
            score1 += int(id)
        if rex2.match(id):
            score2 += int(id)

print(f"{score1=}")
print(f"{score2=}")
