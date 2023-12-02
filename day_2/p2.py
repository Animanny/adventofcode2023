import re

MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14 


def get_power_of_set(sets):
    min_red, min_blue, min_green = 0,0,0
    for set in sets:
            pulls = set.split(", ")
            for colour in pulls:
                if 'blue' in colour:
                    if int(colour.split(" blue")[0]) > min_blue:
                        min_blue = int(colour.split(" blue")[0])
                elif 'red' in colour:
                    if int(colour.split(" red")[0]) > min_red:
                        min_red = int(colour.split(" red")[0]) 
                else:
                    if int(colour.split(" green")[0]) > min_green:
                        min_green = int(colour.split(" green")[0])


    return min_green * min_red * min_blue

tot = 0
with open("./in.txt", "r") as file:
    for line in file:
        line = line.strip()
        game, sets = line.split(": ")
        game = int(re.sub(r"\D", "", game))
        sets = sets.split("; ")
        tot += get_power_of_set(sets)

print(tot)
