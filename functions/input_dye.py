#input dye

#imports
from lists import all_dyes_list

dye="not working"
#input dye
def inputdye():
    global dye
    while True:
        dye=input("Which dye would you like to select?: ")
        dye=dye.lower()
        if dye not in all_dyes_list.dyes:
            print("That dye doesn't exist!")
        else:
            break
    return dye

def getdye():
    return dye

inputdye()