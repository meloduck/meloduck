#input vincent boost

#imports
from functions import input_vincent_multiplier_amount

vincentmultiplier=1

#is dye boosted?
def inputvincentboosted():
    while True:
        vincentboosted=input("Is this Dye currently being boosted by Vincent? (Yes/No): ")
        vincentboosted=vincentboosted.lower()
        if vincentboosted=="yes":
            
            break
        elif vincentboosted=="no":
            break
        else:
            print("Invalid input! Please type 'Yes' or 'No'!")
    return(vincentboosted)