with open("day1/input.txt", "r") as f:
    rotations = f.read().strip().split("\n")

dial = 50
score1, score2 = 0, 0
for rot in rotations:
    amount = int(rot[1:]) * ((rot[0] == "R") * 2 - 1)
    is_zero_departure_to_left = (dial == 0) and (amount < 0)  # Doesn't click
    zero_passes, dial = divmod(dial + amount, 100)
    is_zero_arrival_from_right = (dial == 0) and (amount < 0)  # Does click
    score1 += dial == 0  # day 1
    score2 += (
        abs(zero_passes) - is_zero_departure_to_left + is_zero_arrival_from_right
    )  # day 2

print(f"{score1=}")
print(f"{score2=}")
