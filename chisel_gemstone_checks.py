#chisel gemstone checks

#defaults
chiselgemstone1type=""
chiselgemstone1tier=""
chiselgemstone2type=""
chiselgemstone2tier=""
chiselgemstone3type=""
chiselgemstone3tier=""
aquamarinemultiplier=0
citrinemultiplier=0
onyxmultiplier=0

#check gemstone slot 1 type
def checkgemslot1type():
    global chiselgemstone1type

    while True:
        chiselgemstone1type=input("What type of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
        chiselgemstone1type=chiselgemstone1type.lower()
        if chiselgemstone1type=="aquamarine":
            break
        elif chiselgemstone1type=="citrine":
            break
        elif chiselgemstone1type=="onyx":
            break
        else:
            print("Invalid input!")
    return chiselgemstone1type
    
#check gemstone slot 1 tier
def checkgemslot1tier():
    global chiselgemstone1type
    global chiselgemstone1tier
    global aquamarinemultiplier
    global citrinemultiplier
    global onyxmultiplier

    while True:
        chiselgemstone1tier=input("What tier of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
        chiselgemstone1tier=chiselgemstone1tier.lower()
        if chiselgemstone1tier=="1" or chiselgemstone1tier=="tier 1" or chiselgemstone1tier=="rough" or chiselgemstone1tier=="common" or chiselgemstone1tier=="grey" or chiselgemstone1tier=="gray":
            if chiselgemstone1type=="aquamarine":
                aquamarinemultiplier+=30
                break
            elif chiselgemstone1type=="citrine":
                citrinemultiplier+=30
                break
            elif chiselgemstone1type=="onyx":
                onyxmultiplier+=30
                break
        elif chiselgemstone1tier=="2" or chiselgemstone1tier=="tier 2" or chiselgemstone1tier=="flawed" or chiselgemstone1tier=="uncommon" or chiselgemstone1tier=="green":
            if chiselgemstone1type=="aquamarine":
                aquamarinemultiplier+=40
                break
            elif chiselgemstone1type=="citrine":
                citrinemultiplier+=40
                break
            elif chiselgemstone1type=="onyx":
                onyxmultiplier+=40
                break
        elif chiselgemstone1tier=="3" or chiselgemstone1tier=="tier 3" or chiselgemstone1tier=="fine" or chiselgemstone1tier=="rare" or chiselgemstone1tier=="blue":
            if chiselgemstone1type=="aquamarine":
                aquamarinemultiplier+=50
                break
            elif chiselgemstone1type=="citrine":
                citrinemultiplier+=50
                break
            elif chiselgemstone1type=="onyx":
                onyxmultiplier+=50
                break
        elif chiselgemstone1tier=="4" or chiselgemstone1tier=="tier 4" or chiselgemstone1tier=="flawless" or chiselgemstone1tier=="epic" or chiselgemstone1tier=="purple":
            if chiselgemstone1type=="aquamarine":
                aquamarinemultiplier+=60
                break
            elif chiselgemstone1type=="citrine":
                citrinemultiplier+=60
                break
            elif chiselgemstone1type=="onyx":
                onyxmultiplier+=60
                break
        elif chiselgemstone1tier=="5" or chiselgemstone1tier=="tier 5" or chiselgemstone1tier=="perfect" or chiselgemstone1tier=="legendary" or chiselgemstone1tier=="gold" or chiselgemstone1tier=="orange":
            if chiselgemstone1type=="aquamarine":
                aquamarinemultiplier+=100
                break
            elif chiselgemstone1type=="citrine":
                citrinemultiplier+=100
                break
            elif chiselgemstone1type=="onyx":
                onyxmultiplier+=100
                break
        else:
            print("Invalid input!")
    return(chiselgemstone1type,chiselgemstone1tier,aquamarinemultiplier,citrinemultiplier,onyxmultiplier)

#check gemstone slot 2 type
def checkgemslot2type():
    global chiselgemstone2type

    while True:
        chiselgemstone2type=input("What type of Gemstone do you have in the 2nd Gemstone Slot of your Chisel?: ")
        chiselgemstone2type=chiselgemstone2type.lower()
        if chiselgemstone2type=="aquamarine":
            break
        elif chiselgemstone2type=="citrine":
            break
        elif chiselgemstone2type=="onyx":
            break
        else:
            print("Invalid input!")
    return chiselgemstone2type

#check gemstone slot 2 tier
def checkgemslot2tier():
    global chiselgemstone2type
    global chiselgemstone2tier
    global aquamarinemultiplier
    global citrinemultiplier
    global onyxmultiplier

    while True:
        chiselgemstone2tier=input("What tier of Gemstone do you have in the 2nd Gemstone Slot of your Chisel?: ")
        chiselgemstone2tier=chiselgemstone2tier.lower()
        if chiselgemstone2tier=="1" or chiselgemstone2tier=="tier 1" or chiselgemstone2tier=="rough" or chiselgemstone2tier=="common" or chiselgemstone2tier=="grey" or chiselgemstone2tier=="gray":
            if chiselgemstone2type=="aquamarine":
                aquamarinemultiplier+=30
                break
            elif chiselgemstone2type=="citrine":
                citrinemultiplier+=30
                break
            elif chiselgemstone2type=="onyx":
                onyxmultiplier+=30
                break
        elif chiselgemstone2tier=="2" or chiselgemstone2tier=="tier 2" or chiselgemstone2tier=="flawed" or chiselgemstone2tier=="uncommon" or chiselgemstone2tier=="green":
            if chiselgemstone2type=="aquamarine":
                aquamarinemultiplier+=40
                break
            elif chiselgemstone2type=="citrine":
                citrinemultiplier+=40
                break
            elif chiselgemstone2type=="onyx":
                onyxmultiplier+=40
                break
        elif chiselgemstone2tier=="3" or chiselgemstone2tier=="tier 3" or chiselgemstone2tier=="fine" or chiselgemstone2tier=="rare" or chiselgemstone2tier=="blue":
            if chiselgemstone2type=="aquamarine":
                aquamarinemultiplier+=50
                break
            elif chiselgemstone2type=="citrine":
                citrinemultiplier+=50
                break
            elif chiselgemstone2type=="onyx":
                onyxmultiplier+=50
                break
        elif chiselgemstone2tier=="4" or chiselgemstone2tier=="tier 4" or chiselgemstone2tier=="flawless" or chiselgemstone2tier=="epic" or chiselgemstone2tier=="purple":
            if chiselgemstone2type=="aquamarine":
                aquamarinemultiplier+=60
                break
            elif chiselgemstone2type=="citrine":
                citrinemultiplier+=60
                break
            elif chiselgemstone2type=="onyx":
                onyxmultiplier+=60
                break
        elif chiselgemstone2tier=="5" or chiselgemstone2tier=="tier 5" or chiselgemstone2tier=="perfect" or chiselgemstone2tier=="legendary" or chiselgemstone2tier=="gold" or chiselgemstone2tier=="orange":
            if chiselgemstone2type=="aquamarine":
                aquamarinemultiplier+=100
                break
            elif chiselgemstone2type=="citrine":
                citrinemultiplier+=100
                break
            elif chiselgemstone2type=="onyx":
                onyxmultiplier+=100
                break
        else:
            print("Invalid input!")
    return(chiselgemstone2type,chiselgemstone2tier,aquamarinemultiplier,citrinemultiplier,onyxmultiplier)

#check gemstone slot 3 type
def checkgemslot3type():
    global chiselgemstone3type

    while True:
        chiselgemstone3type=input("What type of Gemstone do you have in the 3rd Gemstone Slot of your Chisel?: ")
        chiselgemstone3type=chiselgemstone3type.lower()
        if chiselgemstone3type=="aquamarine":
            break
        elif chiselgemstone3type=="citrine":
            break
        elif chiselgemstone3type=="onyx":
            break
        else:
            print("Invalid input!")
    return chiselgemstone3type

#check gemstone slot 3 tier
def checkgemslot3tier():
    global chiselgemstone3type
    global chiselgemstone3tier
    global aquamarinemultiplier
    global citrinemultiplier
    global onyxmultiplier

    while True:
        chiselgemstone3tier=input("What tier of Gemstone do you have in the 3rd Gemstone Slot of your Chisel?: ")
        chiselgemstone3tier=chiselgemstone3tier.lower()
        if chiselgemstone3tier=="1" or chiselgemstone3tier=="tier 1" or chiselgemstone3tier=="rough" or chiselgemstone3tier=="common" or chiselgemstone3tier=="grey" or chiselgemstone3tier=="gray":
            if chiselgemstone3type=="aquamarine":
                aquamarinemultiplier+=30
                break
            elif chiselgemstone3type=="citrine":
                citrinemultiplier+=30
                break
            elif chiselgemstone3type=="onyx":
                onyxmultiplier+=30
                break
        elif chiselgemstone3tier=="2" or chiselgemstone3tier=="tier 2" or chiselgemstone3tier=="flawed" or chiselgemstone3tier=="uncommon" or chiselgemstone3tier=="green":
            if chiselgemstone3type=="aquamarine":
                aquamarinemultiplier+=40
                break
            elif chiselgemstone3type=="citrine":
                citrinemultiplier+=40
                break
            elif chiselgemstone3type=="onyx":
                onyxmultiplier+=40
                break
        elif chiselgemstone3tier=="3" or chiselgemstone3tier=="tier 3" or chiselgemstone3tier=="fine" or chiselgemstone3tier=="rare" or chiselgemstone3tier=="blue":
            if chiselgemstone3type=="aquamarine":
                aquamarinemultiplier+=50
                break
            elif chiselgemstone3type=="citrine":
                citrinemultiplier+=50
                break
            elif chiselgemstone3type=="onyx":
                onyxmultiplier+=50
                break
        elif chiselgemstone3tier=="4" or chiselgemstone3tier=="tier 4" or chiselgemstone3tier=="flawless" or chiselgemstone3tier=="epic" or chiselgemstone3tier=="purple":
            if chiselgemstone3type=="aquamarine":
                aquamarinemultiplier+=60
                break
            elif chiselgemstone3type=="citrine":
                citrinemultiplier+=60
                break
            elif chiselgemstone3type=="onyx":
                onyxmultiplier+=60
                break
        elif chiselgemstone3tier=="5" or chiselgemstone3tier=="tier 5" or chiselgemstone3tier=="perfect" or chiselgemstone3tier=="legendary" or chiselgemstone3tier=="gold" or chiselgemstone3tier=="orange":
            if chiselgemstone3type=="aquamarine":
                aquamarinemultiplier+=100
                break
            elif chiselgemstone3type=="citrine":
                citrinemultiplier+=100
                break
            elif chiselgemstone3type=="onyx":
                onyxmultiplier+=100
                break
        else:
            print("Invalid input!")
    return(chiselgemstone3type,chiselgemstone3tier,aquamarinemultiplier,citrinemultiplier,onyxmultiplier)
