import random

n = int(input("Quanti lanci vuoi simulare? "))

for _ in range(n):
    if random.randint(0, 1) == 0:
        print("|", end="")
    else:
        print(" ", end="")