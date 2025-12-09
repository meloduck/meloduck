#imports
from functions import test_affected_mf
magicfindaffected=test_affected_mf.testmfaffected()
magicfind=0

#input magic find
def inputmf():
    if magicfindaffected==True:
        while True:
            global magicfind
            magicfind=input("How much Magic Find do you have?: ")
            try:
                magicfind=int(magicfind)
            except:
                print("Invalid input!")
            if magicfind>=0:
                break
            elif magicfind<0:
                print("You can't have negative Magic Find!")
    return magicfind