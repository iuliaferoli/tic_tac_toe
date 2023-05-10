import random

for i in range(0, 3):
    for j in range(0, 3):
        turn = random.choice(["X", "O"])
        print(turn + " ", end='')
    print()