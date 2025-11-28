#input rng meter and amount of xp and test for int, if not int return "Invalid input!" and try again

#imports
from functions import test_affected_rngmeter
rngaffected=test_affected_rngmeter.testrngaffected()

rngmeteramount=0

#input rng meter amount
def inputrngmeter():
    global rngmeteramount
    if rngaffected==True:
        while True:
            rngmeteramount=input("How much Slayer XP is in your RNG-Meter?: ")
            try:
                rngmeteramount=int(rngmeteramount)
                if rngmeteramount>=0:
                    break
                elif rngmeteramount<0:
                    print("You can't have negative Slayer XP in your RNG-Meter!")
            except:
                print("Invalid input!")
    return rngmeteramount

#input rng meter selected
def inputrngmeterselected():
    rngmeter=False
    if rngaffected==True:
        while True:
            rngmeter=input("Do you have this Dye selected on your RNG-Meter? (Yes/No): ")
            rngmeter=rngmeter.lower()
            if rngmeter=="yes":
                inputrngmeter()
                break
            elif rngmeter=="no":
                break
            else:
                print("Invalid input! Please type 'Yes' or 'No'!")
    return rngmeter

def getrngmeteramount():
    return rngmeteramount