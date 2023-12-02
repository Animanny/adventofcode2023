import re

MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14 


def isGameValid(sets):
    for set in sets:
            pulls = set.split(", ")
            for colour in pulls:
                if 'blue' in colour:
                    if int(colour.split(" blue")[0]) > MAX_BLUE:
                        return False
                elif 'red' in colour:
                    if int(colour.split(" red")[0]) > MAX_RED:
                        return False
                else:
                    if int(colour.split(" green")[0]) > MAX_GREEN:
                        return False

    return True

tot = 0
with open("./in.txt", "r") as file:
    for line in file:
        line = line.strip()
        game, sets = line.split(": ")
        game = int(re.sub(r"\D", "", game))
        sets = sets.split("; ")
        if isGameValid(sets):
            tot += game

print(tot)
