#imports
from functions import test_affected_mf
magicfindaffected=test_affected_mf.testmfaffected()
legionlevel=0

#input legion level
def inputlegion():
    global legionlevel
    if magicfindaffected==True:
        while True:  
            legionlevel=input("What level of Legion do you have?: ")
            try:
                legionlevel=int(legionlevel)
            except:
                print("Invalid input")
            if legionlevel>=0:
                break
            elif legionlevel<0:
                print("You can't have a negative level of Legion!")
            elif legionlevel>20:
                print("You can't have a Legion level higher than 20!")
    return legionlevel

def getlegion():
    return legionlevel