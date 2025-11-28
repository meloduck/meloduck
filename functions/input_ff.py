#input farming fortune and test for int, if not int return "Invalid input!" and try again

#imports
from functions import test_affected_ff

farmingfortuneaffected=test_affected_ff.testffaffected()

def inputff():
    #input farming fortune
    farmingfortune=0
    while True:
        farmingfortune=input("How much Farming Fortune do you have? (With Vacuum equipped!): ")
        try:
            farmingfortune=int(farmingfortune)
            if farmingfortune>=0:
                break
            elif farmingfortune<0:
                print("You can't have negative Farming Fortune!")
        except:
            print("Invalid input!")
    return farmingfortune
            
