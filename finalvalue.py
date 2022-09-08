operations = ["--X", "X++", "X++"]

opPoss = {
    "X++": 1,
    "++X": 1,
    "X--": -1,
    "--X": -1
}
x = 0
for o in operations:
    print(opPoss[o])
    x += opPoss[o]
