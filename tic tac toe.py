#tic tac toe

#to do:
     #figure out how to detect when someone wins

#game
a=" "
b=" "
c=" "
d=" "
e=" "
f=" "
g=" "
h=" "
i=" "

circle="o"
cross="x"
turn=True

isturn=cross

while True:
    if turn:
        turn=False
        isturn=cross
    else:
        turn=True
        isturn=circle
    z=f"[{a}] [{b}] [{c}]\n[{d}] [{e}] [{f}]\n[{g}] [{h}] [{i}]"
    print(z)
    userinput=input(f"\nIn which square would you like to place an {isturn}? ")
    match userinput:
        case "1":
            if a==" ":
                a=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case "2":
            if b==" ":
                b=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case "3":
            if c==" ":
                c=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case "4":
            if d==" ":
                d=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case "5":
            if e==" ":
                e=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case "6":
            if f==" ":
                f=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case "7":
            if g==" ":
                g=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case "8":
            if h==" ":
                h=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case "9":
            if i==" ":
                i=isturn
            else:
                print("There's already something there!")
                turn=not turn
        case _:
            print("Choose an available square, try again:")
            turn=not turn

#win detection
