import re
tot = 0
with open("in.txt", "r") as file:
    for line in file:
        line = re.sub('\D', '', line)
        tot += int(line[0]) * 10 + int(line[-1])

print(tot)