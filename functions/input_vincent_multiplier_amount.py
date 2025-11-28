#input vincent boost amount

#imports

#boosted by how much?
def inputvincentmultiplier():
    while True:
        vincentmultiplier=input("By how much? (...x): ")
        vincentmultiplier=vincentmultiplier.lower()
        if vincentmultiplier=="2x"or vincentmultiplier=="x2"or vincentmultiplier=="2":
            vincentmultiplier=2
            break
        elif vincentmultiplier=="3x"or vincentmultiplier=="x3"or vincentmultiplier=="3":
            vincentmultiplier=3
            break
        else:
            print("Invalid input! Please type '2x' or '3x'!")
    return vincentmultiplier