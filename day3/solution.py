with open("day3/input.txt", "r") as f:
    banks = f.read().strip().split("\n")

N_BATTERIES = 12  # part1: 2, part2: 12

score = 0
for bank in banks:
    batteries = []
    while len(batteries) < N_BATTERIES - 1:
        pickable = bank[: -(N_BATTERIES - len(batteries)) + 1]
        batteries.append(max(pickable))
        bank = bank[bank.index(batteries[-1]) + 1 :]
    batteries.append(max(bank))
    score += int("".join(batteries))
print(f"{score=}")
