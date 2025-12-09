#imports
from functions import input_legion
from functions import test_affected_mf

magicfindaffected=test_affected_mf.testmfaffected()
legionamount=0

#input amount of people close
def inputlegionamount(legionlevel): 
    if magicfindaffected==True:
        if legionlevel>0:
            while True:
                global legionamount
                legionamount=input("How many people are close to you?: ")
                try:
                    legionamount=int(legionamount)
                except:
                    print("Invalid Input")
                if legionamount>=0:
                    break
                elif legionamount<0:
                    print("There can't be negative people close to you!")
                elif legionamount>20:
                    legionamount=20 
                    break
    return legionamount
    