#imports
from functions import test_affected_mf
magicfindaffected=test_affected_mf.testmfaffected()
lootinglevel=0

#input looting level
def inputlooting():
    if magicfindaffected==True:
        while True:
            global lootinglevel
            lootinglevel=input("What level of Looting do you have?: ")
            try:
                lootinglevel=int(lootinglevel)
            except:
                print("Invalid input!")
            if lootinglevel>=0:
                break
            elif lootinglevel<0:
                print("You can't have a negative level of Looting!")
            elif lootinglevel>5:
                print("You can't have a Looting level higher than 5!")
    return lootinglevel