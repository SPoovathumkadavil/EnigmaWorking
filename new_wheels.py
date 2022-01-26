import random

abases = []
for i in range(5):
    base = list("abcdefghijklmnopqrstuvwxyz")
    tbase = []

    for i in range(len(base)):
        r = random.randint(0, len(base)-1)

        tbase.append(base.pop(r))

    tbase_s = ""
    for i in tbase:
        tbase_s += i

    abases.append(tbase_s)

for i in range(len(abases)):
    if(i != len(abases)-1):
        abases[i] += "\n"

wheel_file = open("wheels/wheels.txt", "w")
wheel_file.writelines(abases)
