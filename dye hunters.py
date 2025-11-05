#dye calculator
    #a handy thingy to calculate your dye chances(and maybe estimated time required to drop one in the future)
    #info is mainly pulled from The Official Hypixel Skyblock Wiki and the (unofficial) Hypixel Skyblock Dyes discord server
    #please note that very little is known about how the various items/stats that affect the chance of dye drops work exactly, due to this anything that comes out of this calculator could not be true
    #this calculator is now relatively close to being finished



#to do:
    #make rng meter functional
    #test fossil dye optimizations!!!
    #add time estimates to all dyes maybe
    #make things prettier
    #gaurdian pet for nadeshiko!!
    #look into exporting it as an exe file
    #functions!
    #add relevant attributes!
    #distribute thru different files to make finding things easier
    #make it so it doesn't ask for bucket of dye if the dye doesn't use it
    #look into not doing // and +1 for dye calculations



#imports
#none lol



#all droppable dyes list
dyes=[
    "aquamarine",
    "archfiend",
    "bone",
    "brick red",
    "byzantium",
    "carmine",
    "celadon",
    "celeste",
    "copper",
    "cyclamen",
    "dark purple",
    "dung",
    "emerald",
    "flame",
    "fossil",
    "frostbitten",
    "holly",
    "iceberg",
    "jade",
    "livid",
    "mango",
    "matcha",
    "midnight",
    "mocha",
    "mythological",
    "nadeshiko",
    "necron",
    "nyanza",
    "pearlescent",
    "pelt",
    "periwinkle",
    "sangria",
    "secret",
    "tentacle",
    "treasure",
    "wild strawberry"]

#magic find affected list
mfList=[
    "aquamarine",
    "bone",
    "carmine",
    "cyclamen",
    "iceberg",
    "midnight",
    "pearlescent",
    "periwinkle"]

#farming fortune affected list
ffList=[
    "dung"]

#rng meter (affected) list
rngList=[
    "brick red",
    "byzantium",
    "celeste",
    "flame",
    "jade",
    "livid",
    "matcha",
    "nadeshiko",
    "necron",
    "sangria"]



#functions
#test if input is a integer, if not it makes it an integer if it can, else it returns an error and makes you try again
def testint(prompt):
    userinput=0

    while True:
        userinput=input(f"How much {prompt} Fortune do you have? (With Vacuum equipped!): ")
        try:
            userinput=int(userinput)
            if userinput>=0:
                break
            elif userinput<0:
                print(f"You can't have negative {prompt} Fortune!")
        except:
            print("Invalid input!")
    return userinput

#check gemstone slot 1 type
def checkgemslot1type():
    chiselgemstone1=""

    while True:
        chiselgemstone1=input("What type of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
        chiselgemstone1=chiselgemstone1.lower()
        if chiselgemstone1=="aquamarine":
            break
        elif chiselgemstone1=="citrine":
            break
        elif chiselgemstone1=="onyx":
            break
        else:
            print("Invalid input!")
    return chiselgemstone1
    
#check gemstone slot 1 tier
def checkgemslot1tier():
    chiselgemstonetier1=""
    aquamarinemultiplier=0
    citrinemultiplier=0
    onyxmultiplier=0

    while True:
        chiselgemstonetier1=input("What tier of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
        chiselgemstonetier1=chiselgemstonetier1.lower()
        if chiselgemstonetier1=="1" or chiselgemstonetier1=="tier 1" or chiselgemstonetier1=="rough" or chiselgemstonetier1=="common" or chiselgemstonetier1=="grey" or chiselgemstonetier1=="gray":
            if chiselgemstone1=="aquamarine":
                aquamarinemultiplier+=30
                break
            elif chiselgemstone1=="citrine":
                citrinemultiplier+=30
                break
            elif chiselgemstone1=="onyx":
                onyxmultiplier+=30
                break
        elif chiselgemstonetier1=="2" or chiselgemstonetier1=="tier 2" or chiselgemstonetier1=="flawed" or chiselgemstonetier1=="uncommon" or chiselgemstonetier1=="green":
            if chiselgemstone1=="aquamarine":
                aquamarinemultiplier+=40
                break
            elif chiselgemstone1=="citrine":
                citrinemultiplier+=40
                break
            elif chiselgemstone1=="onyx":
                onyxmultiplier+=40
                break
        elif chiselgemstonetier1=="3" or chiselgemstonetier1=="tier 3" or chiselgemstonetier1=="fine" or chiselgemstonetier1=="rare" or chiselgemstonetier1=="blue":
            if chiselgemstone1=="aquamarine":
                aquamarinemultiplier+=50
                break
            elif chiselgemstone1=="citrine":
                citrinemultiplier+=50
                break
            elif chiselgemstone1=="onyx":
                onyxmultiplier+=50
                break
        elif chiselgemstonetier1=="4" or chiselgemstonetier1=="tier 4" or chiselgemstonetier1=="flawless" or chiselgemstonetier1=="epic" or chiselgemstonetier1=="purple":
            if chiselgemstone1=="aquamarine":
                aquamarinemultiplier+=60
                break
            elif chiselgemstone1=="citrine":
                citrinemultiplier+=60
                break
            elif chiselgemstone1=="onyx":
                onyxmultiplier+=60
                break
        elif chiselgemstonetier1=="5" or chiselgemstonetier1=="tier 5" or chiselgemstonetier1=="perfect" or chiselgemstonetier1=="legendary" or chiselgemstonetier1=="gold" or chiselgemstonetier1=="orange":
            if chiselgemstone1=="aquamarine":
                aquamarinemultiplier+=100
                break
            elif chiselgemstone1=="citrine":
                citrinemultiplier+=100
                break
            elif chiselgemstone1=="onyx":
                onyxmultiplier+=100
                break
        else:
            print("Invalid input!")
    return(chiselgemstone1,chiselgemstonetier1,aquamarinemultiplier,citrinemultiplier,onyxmultiplier)

#check gemstone slot 2 type
def checkgemslot2type():
    chiselgemstone2=""
    
    while True:
        chiselgemstone2=input("What type of Gemstone do you have in the 2nd Gemstone Slot of your Chisel?: ")
        chiselgemstone2=chiselgemstone2.lower()
        if chiselgemstone2=="aquamarine":
            break
        elif chiselgemstone2=="citrine":
            break
        elif chiselgemstone2=="onyx":
            break
        else:
            print("Invalid input!")
    return chiselgemstone2

#check gemstone slot 2 tier
def checkgemslot2tier():
    while True:
        chiselgemstonetier2=input("What tier of Gemstone do you have in the 2nd Gemstone Slot of your Chisel?: ")
        chiselgemstonetier2=chiselgemstonetier2.lower()
        if chiselgemstonetier2=="1" or chiselgemstonetier2=="tier 1" or chiselgemstonetier2=="rough" or chiselgemstonetier2=="common" or chiselgemstonetier2=="grey" or chiselgemstonetier2=="gray":
            if chiselgemstone2=="aquamarine":
                aquamarinemultiplier+=30
                break
            elif chiselgemstone2=="citrine":
                citrinemultiplier+=30
                break
            elif chiselgemstone2=="onyx":
                onyxmultiplier+=30
                break
        elif chiselgemstonetier2=="2" or chiselgemstonetier2=="tier 2" or chiselgemstonetier2=="flawed" or chiselgemstonetier2=="uncommon" or chiselgemstonetier2=="green":
            if chiselgemstone2=="aquamarine":
                aquamarinemultiplier+=40
                break
            elif chiselgemstone2=="citrine":
                citrinemultiplier+=40
                break
            elif chiselgemstone2=="onyx":
                onyxmultiplier+=40
                break
        elif chiselgemstonetier2=="3" or chiselgemstonetier2=="tier 3" or chiselgemstonetier2=="fine" or chiselgemstonetier2=="rare" or chiselgemstonetier2=="blue":
            if chiselgemstone2=="aquamarine":
                aquamarinemultiplier+=50
                break
            elif chiselgemstone2=="citrine":
                citrinemultiplier+=50
                break
            elif chiselgemstone2=="onyx":
                onyxmultiplier+=50
                break
        elif chiselgemstonetier2=="4" or chiselgemstonetier2=="tier 4" or chiselgemstonetier2=="flawless" or chiselgemstonetier2=="epic" or chiselgemstonetier2=="purple":
            if chiselgemstone2=="aquamarine":
                aquamarinemultiplier+=60
                break
            elif chiselgemstone2=="citrine":
                citrinemultiplier+=60
                break
            elif chiselgemstone2=="onyx":
                onyxmultiplier+=60
                break
        elif chiselgemstonetier2=="5" or chiselgemstonetier2=="tier 5" or chiselgemstonetier2=="perfect" or chiselgemstonetier2=="legendary" or chiselgemstonetier2=="gold" or chiselgemstonetier2=="orange":
            if chiselgemstone2=="aquamarine":
                aquamarinemultiplier+=100
                break
            elif chiselgemstone2=="citrine":
                citrinemultiplier+=100
                break
            elif chiselgemstone2=="onyx":
                onyxmultiplier+=100
                break
        else:
            print("Invalid input!")
    return(chiselgemstone2,chiselgemstonetier2,aquamarinemultiplier,citrinemultiplier,onyxmultiplier)

#check gemstone slot 3 type
def checkgemslot3type():
    while True:
        chiselgemstone3=input("What type of Gemstone do you have in the 3rd Gemstone Slot of your Chisel?: ")
        chiselgemstone3=chiselgemstone3.lower()
        if chiselgemstone3=="aquamarine":
            break
        elif chiselgemstone3=="citrine":
            break
        elif chiselgemstone3=="onyx":
            break
        else:
            print("Invalid input!")
    return chiselgemstone3

#check gemstone slot 3 tier
def checkgemslot3tier():
    while True:
        chiselgemstonetier3=input("What tier of Gemstone do you have in the 3rd Gemstone Slot of your Chisel?: ")
        chiselgemstonetier3=chiselgemstonetier3.lower()
        if chiselgemstonetier3=="1" or chiselgemstonetier3=="tier 1" or chiselgemstonetier3=="rough" or chiselgemstonetier3=="common" or chiselgemstonetier3=="grey" or chiselgemstonetier3=="gray":
            if chiselgemstone3=="aquamarine":
                aquamarinemultiplier+=30
                break
            elif chiselgemstone3=="citrine":
                citrinemultiplier+=30
                break
            elif chiselgemstone3=="onyx":
                onyxmultiplier+=30
                break
        elif chiselgemstonetier3=="2" or chiselgemstonetier3=="tier 2" or chiselgemstonetier3=="flawed" or chiselgemstonetier3=="uncommon" or chiselgemstonetier3=="green":
            if chiselgemstone3=="aquamarine":
                aquamarinemultiplier+=40
                break
            elif chiselgemstone3=="citrine":
                citrinemultiplier+=40
                break
            elif chiselgemstone3=="onyx":
                onyxmultiplier+=40
                break
        elif chiselgemstonetier3=="3" or chiselgemstonetier3=="tier 3" or chiselgemstonetier3=="fine" or chiselgemstonetier3=="rare" or chiselgemstonetier3=="blue":
            if chiselgemstone3=="aquamarine":
                aquamarinemultiplier+=50
                break
            elif chiselgemstone3=="citrine":
                citrinemultiplier+=50
                break
            elif chiselgemstone3=="onyx":
                onyxmultiplier+=50
                break
        elif chiselgemstonetier3=="4" or chiselgemstonetier3=="tier 4" or chiselgemstonetier3=="flawless" or chiselgemstonetier3=="epic" or chiselgemstonetier3=="purple":
            if chiselgemstone3=="aquamarine":
                aquamarinemultiplier+=60
                break
            elif chiselgemstone3=="citrine":
                citrinemultiplier+=60
                break
            elif chiselgemstone3=="onyx":
                onyxmultiplier+=60
                break
        elif chiselgemstonetier3=="5" or chiselgemstonetier3=="tier 5" or chiselgemstonetier3=="perfect" or chiselgemstonetier3=="legendary" or chiselgemstonetier3=="gold" or chiselgemstonetier3=="orange":
            if chiselgemstone3=="aquamarine":
                aquamarinemultiplier+=100
                break
            elif chiselgemstone3=="citrine":
                citrinemultiplier+=100
                break
            elif chiselgemstone3=="onyx":
                onyxmultiplier+=100
                break
        else:
            print("Invalid input!")
    return(chiselgemstone3,chiselgemstonetier3,aquamarinemultiplier,citrinemultiplier,onyxmultiplier)



#input dye
while True:
    dye=input("Which dye would you like to select?: ")
    dye=dye.lower()
    if dye not in dyes:
        print("That dye doesn't exist!")
    else:
        break



#input vincent boost
vincentmultiplier=1
while True:
    boost=input("Is this Dye currently being boosted by Vincent? (Yes/No): ")
    boost=boost.lower()
    if boost=="yes":
        while True:
            vincentmultiplierinput=input("By how much? (...x): ")
            if vincentmultiplierinput=="2x"or vincentmultiplierinput=="2":
                vincentmultiplier=2
                break
            elif vincentmultiplierinput=="3x"or vincentmultiplierinput=="3":
                vincentmultiplier=3
                break
            else:
                print("Invalid input!")
        break
    elif boost=="no":
        break
    else:
        print("Invalid input!")



#input bucket of dye
bucketmultiplier=1
while True:
    bucketofdye=input("Do you have a Bucket Of Dye? (Yes/No): ")
    bucketofdye=bucketofdye.lower()
    if bucketofdye=="yes":
        bucketmultiplier=1.01
        break
    elif bucketofdye=="no":
        break
    else:
        print("Please say 'yes' or 'no'!")



#input rng meter
rngmeter=False
rngmeteramount=0
rngmultiplier=1
if dye in rngList:
    while True:
        rngmeter=input("Do you have this Dye selected on your RNG-Meter? (Yes/No): ")
        rngmeter=rngmeter.lower()
        if rngmeter=="yes":
            while True:
                rngmeteramount=input("How much Slayer XP is in your RNG-Meter?: ")
                if rngmeter>=0:
                    break
                elif rngmeteramount<0:
                    print("You can't have negative Slayer XP in your RNG-Meter!")
                else:
                    print("Invalid input!")
        elif rngmeter=="no":
            break
        else:
            print("Invalid input!")



#is the dye affected by magic find (and looting)?
magicfindaffected=False
if dye in mfList:
    magicfindaffected=True

#is the dye affected by farming fortune?
farmingfortuneaffected=False
if dye in ffList:
    farmingfortuneaffected=True

#is the dye affected by RNG meter?
rngaffected=False
if dye in rngList:
    rngaffected=True



#input magic find
magicfind=0
legionlevel=0
legionamount=0
lootinglevel=0
if magicfindaffected==True:
    while True:
        magicfind=input("How much Magic Find do you have?: ")
        try:
            magicfind=int(magicfind)
        except:
            print("Invalid input!")
        if magicfind>=0:
            break
        elif magicfind<0:
            print("You can't have negative Magic Find!")

    #input legion level
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

    #input amount of people close 
    while True:
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

    #input looting level
    while True:
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

lootingmultiplier=(1+lootinglevel*0.15)
magicfind=(magicfind*(0.007*legionamount*legionlevel))
mfmultiplier=(1+magicfind/100)


#input farming fortune
farmingfortune=0
cactusfortune=0
carrotfortune=0
cocoabeansfortune=0
melonfortune=0
mushroomfortune=0
netherwartfortune=0
potatofortune=0
pumpkinfortune=0
sugarcanefortune=0
wheatfortune=0
if farmingfortuneaffected==True:
    while True:
        farmingfortune=input("How much Farming Fortune do you have? (With Vacuum equipped!): ")
        try:
            farmingfortune=int(farmingfortune)
        except:
            print("Invalid input!")
        if farmingfortune>=0:
            break
        elif farmingfortune<0:
            print("You can't have negative Farming Fortune!")

    #input crop fortune
    #cactus
    cactusfortune=testint("Cactus")
    
    #carrot
    carrotfortune=testint("Carrot")

    #cocoabeans
    cocoabeansfortune=testint("Cocoa Beans")

    #melon
    melonfortune=testint("Melon")

    #mushroom
    mushroomfortune=testint("Mushroom")

    #nether wart
    netherwartfortune=testint("Nether Wart")

    #potato
    potatofortune=testint("Potato")

    #pumpkin
    pumpkinfortune=testint("Pumpkin")

    #sugar cane
    sugarcanefortune=testint("Sugar Cane")

    #wheat
    wheatfortune=testint("Wheat")



#fossil dye inputs
chiselcharges=0
aquamarinemultiplier=0
citrinemultiplier=0
onyxmultiplier=0
fungloommultiplier=0
if dye=="fossil":
    #tier of chisel
    while True:
        chisel=input("What tier of Chisel do you have?(From t1 to t4: Chisel, Reinforced Chisel, Glacite-Plated Chisel, Perfect Chisel): ")
        chisel=chisel.lower()
        if chisel=="chisel" or chisel=="t1" or chisel=="1":
            chiselcharges=16
            break
        elif chisel=="reinforced" or chisel=="reinforced chisel" or chisel=="t2" or chisel=="2":
            chiselcharges=18
            break
        elif chisel=="glacite-plated" or chisel=="glacite plated" or chisel=="glacite-plated chisel" or chisel=="glacite plated chisel" or chisel=="t3" or chisel=="3":
            chiselcharges=20
            break
        elif chisel=="perfect" or chisel=="perfect chisel" or chisel=="t4" or chisel=="4":
            chiselcharges=22
            break
        elif chisel=="none" or chisel=="no chisel" or chisel=="no" or chisel=="null" or chisel=="0" or chisel=="nothing":
            print("Then you can't get Fossil Dye!")
            break
        else:
            print("Invalid input!")

    #type and tier of gemstone
    while True:
        #tier 1 chisel
        if chisel=="chisel" or chisel=="t1" or chisel=="1":
            break
        #tier 2 chisel
        elif chisel=="reinforced" or chisel=="reinforced chisel" or chisel=="t2" or chisel=="2":
            #1st slot type
            # chiselgemstone1=checkgemslot1type()
            while True:
                chiselgemstone1=input("What type of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
                chiselgemstone1=chiselgemstone1.lower()
                if chiselgemstone1=="aquamarine":
                    break
                elif chiselgemstone1=="citrine":
                    break
                elif chiselgemstone1=="onyx":
                    break
                else:
                    print("Invalid input!")
            #1st slot tier
            # chiselgemstonetier1=checkgemslot1tier()
            while True:
                chiselgemstonetier1=input("What tier of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
                chiselgemstonetier1=chiselgemstonetier1.lower()
                if chiselgemstonetier1=="1" or chiselgemstonetier1=="tier 1" or chiselgemstonetier1=="rough" or chiselgemstonetier1=="common" or chiselgemstonetier1=="grey" or chiselgemstonetier1=="gray":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=30
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=30
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=30
                        break
                elif chiselgemstonetier1=="2" or chiselgemstonetier1=="tier 2" or chiselgemstonetier1=="flawed" or chiselgemstonetier1=="uncommon" or chiselgemstonetier1=="green":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=40
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=40
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=40
                        break
                elif chiselgemstonetier1=="3" or chiselgemstonetier1=="tier 3" or chiselgemstonetier1=="fine" or chiselgemstonetier1=="rare" or chiselgemstonetier1=="blue":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=50
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=50
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=50
                        break
                elif chiselgemstonetier1=="4" or chiselgemstonetier1=="tier 4" or chiselgemstonetier1=="flawless" or chiselgemstonetier1=="epic" or chiselgemstonetier1=="purple":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=60
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=60
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=60
                        break
                elif chiselgemstonetier1=="5" or chiselgemstonetier1=="tier 5" or chiselgemstonetier1=="perfect" or chiselgemstonetier1=="legendary" or chiselgemstonetier1=="gold" or chiselgemstonetier1=="orange":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=100
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=100
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=100
                        break
                else:
                    print("Invalid input!")

        #tier 3 chisel
        elif chisel=="glacite-plated" or chisel=="glacite plated" or chisel=="glacite-plated chisel" or chisel=="glacite plated chisel" or chisel=="t3" or chisel=="3":
            #1st slot type
            while True:
                chiselgemstone1=input("What type of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
                chiselgemstone1=chiselgemstone1.lower()
                if chiselgemstone1=="aquamarine":
                    break
                elif chiselgemstone1=="citrine":
                    break
                elif chiselgemstone1=="onyx":
                    break
                else:
                    print("Invalid input!")
            #1st slot tier
            while True:
                chiselgemstonetier1=input("What tier of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
                chiselgemstonetier1=chiselgemstonetier1.lower()
                if chiselgemstonetier1=="1" or chiselgemstonetier1=="tier 1" or chiselgemstonetier1=="rough" or chiselgemstonetier1=="common" or chiselgemstonetier1=="grey" or chiselgemstonetier1=="gray":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=30
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=30
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=30
                        break
                elif chiselgemstonetier1=="2" or chiselgemstonetier1=="tier 2" or chiselgemstonetier1=="flawed" or chiselgemstonetier1=="uncommon" or chiselgemstonetier1=="green":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=40
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=40
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=40
                        break
                elif chiselgemstonetier1=="3" or chiselgemstonetier1=="tier 3" or chiselgemstonetier1=="fine" or chiselgemstonetier1=="rare" or chiselgemstonetier1=="blue":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=50
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=50
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=50
                        break
                elif chiselgemstonetier1=="4" or chiselgemstonetier1=="tier 4" or chiselgemstonetier1=="flawless" or chiselgemstonetier1=="epic" or chiselgemstonetier1=="purple":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=60
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=60
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=60
                        break
                elif chiselgemstonetier1=="5" or chiselgemstonetier1=="tier 5" or chiselgemstonetier1=="perfect" or chiselgemstonetier1=="legendary" or chiselgemstonetier1=="gold" or chiselgemstonetier1=="orange":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=100
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=100
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=100
                        break
                else:
                    print("Invalid input!")
            
            #2nd slot type
            while True:
                chiselgemstone2=input("What type of Gemstone do you have in the 2nd Gemstone Slot of your Chisel?: ")
                chiselgemstone2=chiselgemstone2.lower()
                if chiselgemstone2=="aquamarine":
                    break
                elif chiselgemstone2=="citrine":
                    break
                elif chiselgemstone2=="onyx":
                    break
                else:
                    print("Invalid input!")
            #2nd slot tier
            while True:
                chiselgemstonetier2=input("What tier of Gemstone do you have in the 2nd Gemstone Slot of your Chisel?: ")
                chiselgemstonetier2=chiselgemstonetier2.lower()
                if chiselgemstonetier2=="1" or chiselgemstonetier2=="tier 1" or chiselgemstonetier2=="rough" or chiselgemstonetier2=="common" or chiselgemstonetier2=="grey" or chiselgemstonetier2=="gray":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=30
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=30
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=30
                        break
                elif chiselgemstonetier2=="2" or chiselgemstonetier2=="tier 2" or chiselgemstonetier2=="flawed" or chiselgemstonetier2=="uncommon" or chiselgemstonetier2=="green":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=40
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=40
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=40
                        break
                elif chiselgemstonetier2=="3" or chiselgemstonetier2=="tier 3" or chiselgemstonetier2=="fine" or chiselgemstonetier2=="rare" or chiselgemstonetier2=="blue":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=50
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=50
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=50
                        break
                elif chiselgemstonetier2=="4" or chiselgemstonetier2=="tier 4" or chiselgemstonetier2=="flawless" or chiselgemstonetier2=="epic" or chiselgemstonetier2=="purple":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=60
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=60
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=60
                        break
                elif chiselgemstonetier2=="5" or chiselgemstonetier2=="tier 5" or chiselgemstonetier2=="perfect" or chiselgemstonetier2=="legendary" or chiselgemstonetier2=="gold" or chiselgemstonetier2=="orange":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=100
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=100
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=100
                        break
                else:
                    print("Invalid input!")

        #tier 4 chisel
        elif chisel=="perfect" or chisel=="perfect chisel" or chisel=="t4" or chisel=="4":
            #1st slot type
            while True:
                chiselgemstone1=input("What type of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
                chiselgemstone1=chiselgemstone1.lower()
                if chiselgemstone1=="aquamarine":
                    break
                elif chiselgemstone1=="citrine":
                    break
                elif chiselgemstone1=="onyx":
                    break
                else:
                    print("Invalid input!")
            #1st slot tier
            while True:
                chiselgemstonetier1=input("What tier of Gemstone do you have in the 1st Gemstone Slot of your Chisel?: ")
                chiselgemstonetier1=chiselgemstonetier1.lower()
                if chiselgemstonetier1=="1" or chiselgemstonetier1=="tier 1" or chiselgemstonetier1=="rough" or chiselgemstonetier1=="common" or chiselgemstonetier1=="grey" or chiselgemstonetier1=="gray":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=30
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=30
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=30
                        break
                elif chiselgemstonetier1=="2" or chiselgemstonetier1=="tier 2" or chiselgemstonetier1=="flawed" or chiselgemstonetier1=="uncommon" or chiselgemstonetier1=="green":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=40
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=40
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=40
                        break
                elif chiselgemstonetier1=="3" or chiselgemstonetier1=="tier 3" or chiselgemstonetier1=="fine" or chiselgemstonetier1=="rare" or chiselgemstonetier1=="blue":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=50
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=50
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=50
                        break
                elif chiselgemstonetier1=="4" or chiselgemstonetier1=="tier 4" or chiselgemstonetier1=="flawless" or chiselgemstonetier1=="epic" or chiselgemstonetier1=="purple":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=60
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=60
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=60
                        break
                elif chiselgemstonetier1=="5" or chiselgemstonetier1=="tier 5" or chiselgemstonetier1=="perfect" or chiselgemstonetier1=="legendary" or chiselgemstonetier1=="gold" or chiselgemstonetier1=="orange":
                    if chiselgemstone1=="aquamarine":
                        aquamarinemultiplier+=100
                        break
                    elif chiselgemstone1=="citrine":
                        citrinemultiplier+=100
                        break
                    elif chiselgemstone1=="onyx":
                        onyxmultiplier+=100
                        break
                else:
                    print("Invalid input!")

            #2nd slot type
            while True:
                chiselgemstone2=input("What type of Gemstone do you have in the 2nd Gemstone Slot of your Chisel?: ")
                chiselgemstone2=chiselgemstone2.lower()
                if chiselgemstone2=="aquamarine":
                    break
                elif chiselgemstone2=="citrine":
                    break
                elif chiselgemstone2=="onyx":
                    break
                else:
                    print("Invalid input!")
            #2nd slot tier
            while True:
                chiselgemstonetier2=input("What tier of Gemstone do you have in the 2nd Gemstone Slot of your Chisel?: ")
                chiselgemstonetier2=chiselgemstonetier2.lower()
                if chiselgemstonetier2=="1" or chiselgemstonetier2=="tier 1" or chiselgemstonetier2=="rough" or chiselgemstonetier2=="common" or chiselgemstonetier2=="grey" or chiselgemstonetier2=="gray":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=30
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=30
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=30
                        break
                elif chiselgemstonetier2=="2" or chiselgemstonetier2=="tier 2" or chiselgemstonetier2=="flawed" or chiselgemstonetier2=="uncommon" or chiselgemstonetier2=="green":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=40
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=40
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=40
                        break
                elif chiselgemstonetier2=="3" or chiselgemstonetier2=="tier 3" or chiselgemstonetier2=="fine" or chiselgemstonetier2=="rare" or chiselgemstonetier2=="blue":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=50
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=50
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=50
                        break
                elif chiselgemstonetier2=="4" or chiselgemstonetier2=="tier 4" or chiselgemstonetier2=="flawless" or chiselgemstonetier2=="epic" or chiselgemstonetier2=="purple":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=60
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=60
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=60
                        break
                elif chiselgemstonetier2=="5" or chiselgemstonetier2=="tier 5" or chiselgemstonetier2=="perfect" or chiselgemstonetier2=="legendary" or chiselgemstonetier2=="gold" or chiselgemstonetier2=="orange":
                    if chiselgemstone2=="aquamarine":
                        aquamarinemultiplier+=100
                        break
                    elif chiselgemstone2=="citrine":
                        citrinemultiplier+=100
                        break
                    elif chiselgemstone2=="onyx":
                        onyxmultiplier+=100
                        break
                else:
                    print("Invalid input!")

            #3rd slot type
            while True:
                chiselgemstone3=input("What type of Gemstone do you have in the 3rd Gemstone Slot of your Chisel?: ")
                chiselgemstone3=chiselgemstone3.lower()
                if chiselgemstone3=="aquamarine":
                    break
                elif chiselgemstone3=="citrine":
                    break
                elif chiselgemstone3=="onyx":
                    break
                else:
                    print("Invalid input!")
            #3rd slot tier
            while True:
                chiselgemstonetier3=input("What tier of Gemstone do you have in the 3rd Gemstone Slot of your Chisel?: ")
                chiselgemstonetier3=chiselgemstonetier3.lower()
                if chiselgemstonetier3=="1" or chiselgemstonetier3=="tier 1" or chiselgemstonetier3=="rough" or chiselgemstonetier3=="common" or chiselgemstonetier3=="grey" or chiselgemstonetier3=="gray":
                    if chiselgemstone3=="aquamarine":
                        aquamarinemultiplier+=30
                        break
                    elif chiselgemstone3=="citrine":
                        citrinemultiplier+=30
                        break
                    elif chiselgemstone3=="onyx":
                        onyxmultiplier+=30
                        break
                elif chiselgemstonetier3=="2" or chiselgemstonetier3=="tier 2" or chiselgemstonetier3=="flawed" or chiselgemstonetier3=="uncommon" or chiselgemstonetier3=="green":
                    if chiselgemstone3=="aquamarine":
                        aquamarinemultiplier+=40
                        break
                    elif chiselgemstone3=="citrine":
                        citrinemultiplier+=40
                        break
                    elif chiselgemstone3=="onyx":
                        onyxmultiplier+=40
                        break
                elif chiselgemstonetier3=="3" or chiselgemstonetier3=="tier 3" or chiselgemstonetier3=="fine" or chiselgemstonetier3=="rare" or chiselgemstonetier3=="blue":
                    if chiselgemstone3=="aquamarine":
                        aquamarinemultiplier+=50
                        break
                    elif chiselgemstone3=="citrine":
                        citrinemultiplier+=50
                        break
                    elif chiselgemstone3=="onyx":
                        onyxmultiplier+=50
                        break
                elif chiselgemstonetier3=="4" or chiselgemstonetier3=="tier 4" or chiselgemstonetier3=="flawless" or chiselgemstonetier3=="epic" or chiselgemstonetier3=="purple":
                    if chiselgemstone3=="aquamarine":
                        aquamarinemultiplier+=60
                        break
                    elif chiselgemstone3=="citrine":
                        citrinemultiplier+=60
                        break
                    elif chiselgemstone3=="onyx":
                        onyxmultiplier+=60
                        break
                elif chiselgemstonetier3=="5" or chiselgemstonetier3=="tier 5" or chiselgemstonetier3=="perfect" or chiselgemstonetier3=="legendary" or chiselgemstonetier3=="gold" or chiselgemstonetier3=="orange":
                    if chiselgemstone3=="aquamarine":
                        aquamarinemultiplier+=100
                        break
                    elif chiselgemstone3=="citrine":
                        citrinemultiplier+=100
                        break
                    elif chiselgemstone3=="onyx":
                        onyxmultiplier+=100
                        break
                else:
                    print("Invalid input!")
        else:
            break
        break

    #fungloom shard
    while True:
        fungloom=input("What level is your Fungloom attribute?: ")
        if fungloom=="0":
            break
        elif fungloom=="1":
            fungloommultiplier+=10
            break
        elif fungloom=="2":
            fungloommultiplier+=20
            break
        elif fungloom=="3":
            fungloommultiplier+=30
            break
        elif fungloom=="4":
            fungloommultiplier+=40
            break
        elif fungloom=="5":
            fungloommultiplier+=50
            break
        elif fungloom=="6":
            fungloommultiplier+=60
            break
        elif fungloom=="7":
            fungloommultiplier+=70
            break
        elif fungloom=="8":
            fungloommultiplier+=80
            break
        elif fungloom=="9":
            fungloommultiplier+=90
            break
        elif fungloom=="10":
            fungloommultiplier+=100
            break
        elif fungloom<0:
            print("You can't have a negative level of Fungloom!")
        else:
            print("Invalid input!")



#print info
print(f"\n\nSelected Dye: {dye}")
if rngmeter=="yes":
    print(f"Selected on RNG-Meter: {rngmeter}")
    print(f"Amount of XP in RNG-Meter: {rngmeteramount}")
print(f"Boosted by Vincent: {boost}")
if boost=="yes":
    print(f"Boosted by: {vincentmultiplierinput}\n\n")
if dye=="fossil":
    print(f"Chisel tier: {chisel}\n")
    if chisel=="reinforced" or chisel=="reinforced chisel" or chisel=="t2" or chisel=="2":
        print(f"Gemstone type: {chiselgemstone1}")
        print(f"Gemstone tier: {chiselgemstonetier1}\n")
    elif chisel=="glacite-plated" or chisel=="glacite plated" or chisel=="glacite-plated chisel" or chisel=="glacite plated chisel" or chisel=="t3" or chisel=="3":
        print(f"1st slot Gemstone type: {chiselgemstone1}")
        print(f"1st slot Gemstone tier: {chiselgemstonetier1}\n")
        print(f"2nd slot Gemstone type: {chiselgemstone2}")
        print(f"2nd slot Gemstone tier: {chiselgemstonetier2}\n")
    elif chisel=="perfect" or chisel=="perfect chisel" or chisel=="t4" or chisel=="4":
        print(f"1st slot Gemstone type: {chiselgemstone1}")
        print(f"1st slot Gemstone tier: {chiselgemstonetier1}\n")
        print(f"2nd slot Gemstone type: {chiselgemstone2}")
        print(f"2nd slot Gemstone tier: {chiselgemstonetier2}\n")
        print(f"3rd slot Gemstone type: {chiselgemstone3}")
        print(f"3rd slot Gemstone tier: {chiselgemstonetier3}\n")
    print(f"Fungloom Attribute level: {fungloom}\n")
if magicfindaffected==True:
    print(
        f"Magic Find: {magicfind}\n"
        f"Legion level: {legionlevel}\n"
        f"Amount of people close: {legionamount}")
if farmingfortuneaffected==True:
    print(f"\nFarming Fortune: {farmingfortune}")
if magicfindaffected==True:
    print(f"Looting level: {lootinglevel}")



#dye chance calculations

#aquamarine
aquamarinechance1=(0.00002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
aquamarinechance2=(0.00004*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
aquamarinechance3=(0.0002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="aquamarine":
    print("\nChance for Aquamarine Dye:\n"
        f"From Common/Uncommon Water Sea Creatures:     {aquamarinechance1}% or 1/{100//aquamarinechance1+1}\n"
        f"From Rare/Epic Water Sea Creatures:           {aquamarinechance2}% or 1/{100//aquamarinechance2+1}\n"
        f"From Legendary/Mythic Water Sea Creatures:    {aquamarinechance3}% or 1/{100//aquamarinechance3+1}\n")



#archfiend
archfiendchance1=(0.015*bucketmultiplier*vincentmultiplier)
archfiendchance2=(0.15*bucketmultiplier*vincentmultiplier)

if dye=="archfiend":
    print("\nChance for Archfiend Dye:\n"
        f"From rolling an Archfiend Dice:           {archfiendchance1}% or 1/{100//archfiendchance1+1}\n"
        f"From rolling a High Class Archfiend Dice: {archfiendchance2}% or 1/{100//archfiendchance2+1}\n")



#bone
bonechance=(0.0000333*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="bone":
    print("\nChance for Bone Dye:\n"
        f"From any skeletal mob: {bonechance}% or 1/{100//bonechance+1}\n")



#brick red
brickredchance1=(0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier)
brickredchance2=(0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier)
brickredchance3=(0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier)
brickredchance4=(0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="brick red":
    print("\nChance for Brick Red Dye:\n"
          f"From Tier 1 Tarantula Broodfather: {brickredchance1}% or 1/{100//brickredchance1+1}\n"
          f"From Tier 2 Tarantula Broodfather: {brickredchance2}% or 1/{100//brickredchance2+1}\n"
          f"From Tier 3 Tarantula Broodfather: {brickredchance3}% or 1/{100//brickredchance3+1}\n"
          f"From Tier 4 Tarantula Broodfather: {brickredchance4}% or 1/{100//brickredchance4+1}\n")



#byzantium
byzantiumchance1=(0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier)
byzantiumchance2=(0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier)
byzantiumchance3=(0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier)
byzantiumchance4=(0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="byzantium":
    print("\nChance for Byzantium Dye:\n"
        f"From Tier 1 Voidgloom Seraph: {byzantiumchance1}% or 1/{100//byzantiumchance1+1}\n"
        f"From Tier 2 Voidgloom Seraph: {byzantiumchance2}% or 1/{100//byzantiumchance2+1}\n"
        f"From Tier 3 Voidgloom Seraph: {byzantiumchance3}% or 1/{100//byzantiumchance3+1}\n"
        f"From Tier 4 Voidgloom Seraph: {byzantiumchance4}% or 1/{100//byzantiumchance4+1}\n")



#carmine
carminechance1=(0.00002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
carminechance2=(0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
carminechance3=(0.002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="carmine":
    print("\nChance for Carmine Dye:\n"
          f"From Common/Uncommon Lava Sea Creatures:    {carminechance1}% or 1/{100//carminechance1+1}\n"
          f"From Rare/Epic Lava Sea Creatures:          {carminechance2}% or 1/{100//carminechance2+1}\n"
          f"From Legendary/Mythic Lava Sea Creatures:   {carminechance3}% or 1/{100//carminechance3+1}\n")



#celadon
celadonchance1=(0.001*rngmultiplier*vincentmultiplier)
celadonchance2=(0.01*rngmultiplier*vincentmultiplier)

if dye=="celadon":
    print("\nChance for Celadon Dye:\n"
          f"From Blobbercyst:   {celadonchance1}% or 1/{100//celadonchance1+1}\n"
          f"From Bacte:         {celadonchance2}% or 1/{100//celadonchance2+1}\n")



#celeste
celestechance1=(0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier)
celestechance2=(0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier)
celestechance3=(0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier)
celestechance4=(0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="celeste":
    print("\nChance for Celeste Dye:\n"
        f"From Tier 1 Sven Packmaster: {celestechance1}% or 1/{100//celestechance1+1}\n"
        f"From Tier 2 Sven Packmaster: {celestechance2}% or 1/{100//celestechance2+1}\n"
        f"From Tier 3 Sven Packmaster: {celestechance3}% or 1/{100//celestechance3+1}\n"
        f"From Tier 4 Sven Packmaster: {celestechance4}% or 1/{100//celestechance4+1}\n")



#copper
copperchance1=(0.001*bucketmultiplier*vincentmultiplier)
copperchance2=(0.002*bucketmultiplier*vincentmultiplier)
copperchance3=(0.004*bucketmultiplier*vincentmultiplier)
copperchance4=(0.02*bucketmultiplier*vincentmultiplier)
copperchance5=(0.2*bucketmultiplier*vincentmultiplier)

if dye=="copper":
    print("\nChance for Copper Dye:\n"
          f"From Uncommon Visitor:  {copperchance1}% or 1/{100//copperchance1+1}\n"
          f"From Rare Visitor:      {copperchance2}% or 1/{100//copperchance2+1}\n"
          f"From Legendary Visitor: {copperchance3}% or 1/{100//copperchance3+1}\n"
          f"From Mythic Visitor:    {copperchance4}% or 1/{100//copperchance4+1}\n"
          f"From Special Visitor:   {copperchance5}% or 1/{100//copperchance5+1}\n")



#cyclamen
cyclamenchance1=(0.00001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
cyclamenchance2=(0.00004*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
cyclamenchance3=(0.0004*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="cyclamen":
    print("\nChance for Cyclamen Dye:\n\n"
        f"From:\nBezal,/nBlaze,\nFlaming Spider,\nFlare,\nKada Knight,\nMagma Cube,\nMagma Cube Rider,\nMushroom Bull,\nMutated Blaze,\nWither Skeleton,\nWither Spectre:\n{cyclamenchance1}% or 1/{100//cyclamenchance1+1}\n\n"
        f"From:\nBarbarian,\nBarbarian Gaurd,\nDive Ghast,\nFire Mage,\nGhast,\nGoliath Barbarian,\nKrondor Necromancer,\nMage Gaurd,\nMagma Glare,\nMatcho,\nMillenia-Aged Blaze,\nSmoldering Blaze,\nUnstable Magma:\n{cyclamenchance2}% or 1/{100//cyclamenchance2+1}\n\n"
        f"From:\nAshfang,\nBarbarian Duke X,\nBladesoul,\nCinderbat,\nHellwisp,\nMage Outlaw,\nMagma Boss,\nVanquisher:\n{cyclamenchance3}% or 1/{100//cyclamenchance3+1}\n")



#dark purple
darkpurplechance=(0.748*vincentmultiplier)

if dye=="dark purple":
    print("\nChance for Dark Purple Dye:\n"
        f"To appear in a Dark(er) Auction lobby: {darkpurplechance}% or 1/{100//darkpurplechance+1}\n")



#dung
dungchancebeetle=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+netherwartfortune)/600))
dungchancecricket=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+carrotfortune)/600))
dungchanceearthworm=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+melonfortune)/600))
dungchancefieldmouse=(0.001*bucketmultiplier*vincentmultiplier*(1+farmingfortune/600))
dungchancefly=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+wheatfortune)/600))
dungchancelocust=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+potatofortune)/600))
dungchancemite=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+cactusfortune)/600))
dungchancemosquito=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+sugarcanefortune)/600))
dungchancemoth=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+cocoabeansfortune)/600))
dungchancerat=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+pumpkinfortune)/600))
dungchanceslug=(0.0002*bucketmultiplier*vincentmultiplier*(1+(farmingfortune+mushroomfortune)/600))

if dye=="dung":
    print("\nChance for Dung Dye:\n"
        f"From a Beetle:        {dungchancebeetle}% or 1/{100//dungchancebeetle+1}\n"
        f"From a Cricket:       {dungchancecricket}% or 1/{100//dungchancecricket+1}\n"
        f"From an Earthworm:    {dungchanceearthworm}% or 1/{100//dungchanceearthworm+1}\n"
        f"From a Field Mouse:   {dungchancefieldmouse}% or 1/{100//dungchancefieldmouse+1}\n"
        f"From a Fly:           {dungchancefly}% or 1/{100//dungchancefly+1}\n"
        f"From a Locust:        {dungchancelocust}% or 1/{100//dungchancelocust+1}\n"
        f"From a Mite:          {dungchancemite}% or 1/{100//dungchancemite+1}\n"
        f"From a Mosquito:      {dungchancemosquito}% or 1/{100//dungchancemosquito+1}\n"
        f"From a Moth:          {dungchancemoth}% or 1/{100//dungchancemoth+1}\n"
        f"From a Rat:           {dungchancerat}% or 1/{100//dungchancerat+1}\n"
        f"From a Slug:          {dungchanceslug}% or 1/{100//dungchanceslug+1}\n")



#emerald
emeraldchance=(0.00002*bucketmultiplier*vincentmultiplier)

if dye=="emerald":
    print("\nChance for Emerald Dye:\n"
        f"Per Emerald (Ore) broken: {emeraldchance}% or 1/{100//emeraldchance+1}\n")



#flame
flamechance1=(0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier)
flamechance2=(0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier)
flamechance3=(0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier)
flamechance4=(0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="flame":
    print("\nChance for Flame Dye:\n"
        f"From Tier 1 Inferno Demonlord: {flamechance1}% or 1/{100//flamechance1+1}\n"
        f"From Tier 2 Inferno Demonlord: {flamechance2}% or 1/{100//flamechance2+1}\n"
        f"From Tier 3 Inferno Demonlord: {flamechance3}% or 1/{100//flamechance3+1}\n"
        f"From Tier 4 Inferno Demonlord: {flamechance4}% or 1/{100//flamechance4+1}\n")



#fossil
chiselcharges=(chiselcharges+(aquamarinemultiplier/100))
treasures=(11.5+(onyxmultiplier/100)+(fungloommultiplier/100))
highlightedtreasures=(citrinemultiplier/100)

fossilchance=(0.0002*bucketmultiplier*vincentmultiplier)
fossilchanceperscrap=(0.0002*bucketmultiplier*vincentmultiplier*treasures*((chiselcharges-highlightedtreasures)/(54-highlightedtreasures)))

if dye=="fossil":
    print("\nChance for Fossil Dye:\n"
        f"To replace any Treasure in Fossil Excavator:  {fossilchance}% or 1/{100//fossilchance+1}\n"
        f"To BE OBTAINED per scrap:                     {fossilchanceperscrap}% or 1/{100//fossilchanceperscrap+1}\n")



#frostbitten
frostbittenchance1=(0.0004*bucketmultiplier*vincentmultiplier)
frostbittenchance2=(0.001*bucketmultiplier*vincentmultiplier)
frostbittenchance3=(0.01*bucketmultiplier*vincentmultiplier)

if dye=="frostbitten":
    print("\nChance for Frostbitten Dye:\n"
        f"From Lapis Corpse:            {frostbittenchance1}% or 1/{100//frostbittenchance1+1}\n"
        f"From Umber/Tungsten Corpse:   {frostbittenchance2}% or 1/{100//frostbittenchance2+1}\n"
        f"From Vangaurd Corpse:         {frostbittenchance3}% or 1/{100//frostbittenchance3+1}\n")



#holly
hollychance=(0.00125*bucketmultiplier*vincentmultiplier)

if dye=="holly":
    print("\nChance for Holly Dye:\n"
        f"From Red Gift: {hollychance}% or 1/{100//hollychance+1}\n")



#iceberg
icerbergchance1=(0.0001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
icerbergchance2=(0.0002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
icerbergchance3=(0.002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="icerberg":
    print("\nChance for Icerberg Dye:\n\n"
        f"From:\nFrosty,\nFrozen Steve:\n{icerbergchance1}% or 1/{100//icerbergchance1+1}\n\n"
        f"From:\nNutcracker:\n{icerbergchance2}% or 1/{100//icerbergchance2+1}\n\n"
        f"From:\nYeti:{icerbergchance3}% or 1/{100//icerbergchance3+1}\n")



#jade
jadechance=(0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="jade":
    print("\nChance for Jade Dye:\n"
        f"Per item roll in a Crystal Nucleus Bundle: {jadechance}% or 1/{100//jadechance+1}\n")



#livid
lividchance=(0.02*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="livid":
    print("\nChance for Livid Dye:\n"
        f"From Bedrock Chest in Master Catacombs Floor V {lividchance}% or 1/{100//lividchance+1}\n")



#mango
mangochance=(0.00001*bucketmultiplier*vincentmultiplier)

if dye=="mango":
    print("\nChance for Mango Dye:\n"
          f"From breaking any log: {mangochance}% or 1/{100//mangochance+1}\n")



#matcha
matchachance1=(0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier)
matchachance2=(0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier)
matchachance3=(0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier)
matchachance4=(0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier)
matchachance5=(0.0004*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="matcha":
    print("\nChance for Matcha Dye:\n"
        f"From Tier 1 Revenant Horror: {matchachance1}% or 1/{100//matchachance1+1}\n"
        f"From Tier 2 Revenant Horror: {matchachance2}% or 1/{100//matchachance2+1}\n"
        f"From Tier 3 Revenant Horror: {matchachance3}% or 1/{100//matchachance3+1}\n"
        f"From Tier 4 Revenant Horror: {matchachance4}% or 1/{100//matchachance4+1}\n"
        f"From Tier 5 Revenant Horror: {matchachance5}% or 1/{100//matchachance5+1}\n")



#midnight
midnightchance1=(0.0001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
midnightchance2=(0.0002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
midnightchance3=(0.002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="midnight":
    print("\nChance for Midnight Dye:\n\n"
        f"From:\nCrazy Witch,\nPhantom Spirit,\nScary Jerry,\nTrick or Treater,\nWither Gourd,\nWraith:\n{midnightchance1}% or 1/{100//midnightchance1+1}\n\n"
        f"From:\nNightmare,\nScarecrow,\nWerewolf:\n{midnightchance2}% or 1/{100//midnightchance2+1}\n\n"
        f"From:\nGrim Reaper,\nHeadless Horseman,\nPhantom Fisher:\n{midnightchance3}% or 1/{100//midnightchance3+1}\n")



#mocha
mochachance1=(0.000001*bucketmultiplier*vincentmultiplier)
mochachance2=(0.00002*bucketmultiplier*vincentmultiplier)
mochachance3=(0.00004*bucketmultiplier*vincentmultiplier)
mochachance4=(0.0001*bucketmultiplier*vincentmultiplier)
mochachance5=(0.00013*bucketmultiplier*vincentmultiplier)
mochachance6=(0.0002*bucketmultiplier*vincentmultiplier)
mochachance7=(0.0004*bucketmultiplier*vincentmultiplier)
mochachance8=(0.001*bucketmultiplier*vincentmultiplier)

if dye=="mocha":
    print("\nChance for Mocha Dye:\n"
        f"From Level 1 Potions: {mochachance1}% or 1/{100//mochachance1}\n" #no +1 for some reason
        f"From Level 2 Potions: {mochachance2}% or 1/{100//mochachance2+1}\n"
        f"From Level 3 Potions: {mochachance3}% or 1/{100//mochachance3+1}\n"
        f"From Level 4 Potions: {mochachance4}% or 1/{100//mochachance4+1}\n"
        f"From Level 5 Potions: {mochachance5}% or 1/{100//mochachance5+1}\n"
        f"From Level 6 Potions: {mochachance6}% or 1/{100//mochachance6+1}\n"
        f"From Level 7 Potions: {mochachance7}% or 1/{100//mochachance7+1}\n"
        f"From Level 8 Potions: {mochachance8}% or 1/{100//mochachance8+1}\n")



#mythological
mythologicalchance=(0.0001*bucketmultiplier*vincentmultiplier)

if dye=="mythological":
    print("\nChance for Mythological Dye:\n"
        f"From digging up a Treasure Burrow: {mythologicalchance}% or 1/{100//mythologicalchance+1}\n")



#nadeshiko
nadeshikochance1=(0.00133*rngmultiplier*bucketmultiplier*vincentmultiplier)
nadeshikochance2=(0.002*rngmultiplier*bucketmultiplier*vincentmultiplier)
nadeshikochance3=(0.004*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="nadeshiko":
    print("\nChance for Nadeshiko Dye to appear:\n"
        f"In Supreme Superpairs Experiment:         {nadeshikochance1}% or 1/{100//nadeshikochance1+1}\n"
        f"In Transcendent Superpairs Experiment:    {nadeshikochance2}% or 1/{100//nadeshikochance2+1}\n"
        f"In Metaphysical Superpairs Experiment:    {nadeshikochance3}% or 1/{100//nadeshikochance3+1}\n")



#necron
necronchance=(0.04*rngmultiplier*bucketmultiplier*vincentmultiplier)

if dye=="necron":
    print("\nChance for Necron Dye:\n"
        f"From Bedrock Chest in Master Catacombs Floor VII: {necronchance}% or 1/{100//necronchance+1}\n")



#nyanza
nyanzachance=(0.0004*bucketmultiplier*vincentmultiplier)

if dye=="nyanza":
    print("\nChance for Nyanza Dye:\n"
        f"From completing a Commission: {nyanzachance}% or 1/{100//nyanzachance+1}\n")



#pearlescent
pearlescentchance1=(0.00001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
pearlescentchance2=(0.00002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
pearlescentchance3=(0.001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
pearlescentchance4=(0.002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="pearlescent":
    print("\nChance for Pearlescent Dye:\n\n"
        f"From:\nEnderman,\nEndermite,\nObsidiant Defender,\nSeer,\nZealot,\nZealot Bruiser:\n{pearlescentchance1}% or 1/{100//pearlescentchance1+1}\n\n"
        f"From:\nNest Endermite,\nVoidling Extremist,\nVoidling Fenatic:\n{pearlescentchance2}% or 1/{100//pearlescentchance2+1}\n\n"
        f"From:\nEnd Stone Protector,\nOld Dragon,\nProtector Dragon,\nSpecial Zealot,\nStrong Dragon,\nUnstable Dragon,\nWise Dragon,\nYoung Dragon:\n{pearlescentchance3}% or 1/{100//pearlescentchance3+1}\n\n"
        f"From:\nSuperior Dragon:\n{pearlescentchance4}% or 1/{100//pearlescentchance4+1}\n")



#pelt
peltchance1=(0.0004*bucketmultiplier*vincentmultiplier)
peltchance2=(0.0005*bucketmultiplier*vincentmultiplier)
peltchance3=(0.000667*bucketmultiplier*vincentmultiplier)
peltchance4=(0.001*bucketmultiplier*vincentmultiplier)
peltchance5=(0.01*bucketmultiplier*vincentmultiplier)

if dye=="pelt":
    print("\nChance for Pelt Dye:\n"
        f"From a Trackable Animal:      {peltchance1}% or 1/{100//peltchance1+1}\n"
        f"From an Untrackable Animal:   {peltchance2}% or 1/{100//peltchance2+1}\n"
        f"From an Undetected Animal:    {peltchance3}% or 1/{100//peltchance3+1}\n"
        f"From an Endangered Animal:    {peltchance4}% or 1/{100//peltchance4+1}\n"
        f"From an Elusive Animal:       {peltchance5}% or 1/{100//peltchance5+1}\n")



#periwinkle
periwinklechance1=(0.0002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
periwinklechance2=(0.00025*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
periwinklechance3=(0.000333*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
periwinklechance4=(0.0005*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
periwinklechance5=(0.001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="periwinkle":
    print("\nChance for Periwinkle Dye:\n"
        f"From Level 1-99 Runic Mobs:       {periwinklechance1}% or 1/{100//periwinklechance1+1}\n"
        f"From Level 100-199 Runic Mobs:    {periwinklechance2}% or 1/{100//periwinklechance2+1}\n"
        f"From Level 200-299 Runic Mobs:    {periwinklechance3}% or 1/{100//periwinklechance3+1}\n"
        f"From Level 300-399 Runic Mobs:    {periwinklechance4}% or 1/{100//periwinklechance4+1}\n"
        f"From level 400+ Runic Mobs:       {periwinklechance5}% or 1/{100//periwinklechance5+1}\n")



#sangria
sangriachance1=(0.001*rngmultiplier*vincentmultiplier)
sangriachance2=(0.00125*rngmultiplier*vincentmultiplier)
sangriachance3=(0.00167*rngmultiplier*vincentmultiplier)
sangriachance4=(0.0025*rngmultiplier*vincentmultiplier)
sangriachance5=(0.01*rngmultiplier*vincentmultiplier)

if dye=="sangria":
    print("\nChance for Sangria Dye:\n"
        f"From Tier 1 Riftstalker Bloodfiend: {sangriachance1}% or 1/{100//sangriachance1+1}\n"
        f"From Tier 2 Riftstalker Bloodfiend: {sangriachance2}% or 1/{100//sangriachance2+1}\n"
        f"From Toer 3 Riftstalker Bloodfiend: {sangriachance3}% or 1/{100//sangriachance3+1}\n"
        f"From Tier 4 Riftstalker Bloodfiend: {sangriachance4}% or 1/{100//sangriachance4+1}\n"
        f"From Tier 5 Riftstalker Bloodfiend: {sangriachance5}% or 1/{100//sangriachance5+1}\n")



#secret
secretchance=(0.0001*bucketmultiplier*vincentmultiplier)

if dye=="secret":
    print("\nChance for Secret Dye:\n"
        f"From Collecting a Secret: {secretchance}% or 1/{100//secretchance+1}\n")



#tentacle
tentaclechance1=(0.001*bucketmultiplier*vincentmultiplier)
tentaclechance2=(0.00125*bucketmultiplier*vincentmultiplier)
tentaclechance3=(0.00167*bucketmultiplier*vincentmultiplier)
tentaclechance4=(0.0025*bucketmultiplier*vincentmultiplier)
tentaclechance5=(0.005*bucketmultiplier*vincentmultiplier)

if dye=="tentacle":
    print("\nChance for Tentacle Dye:\n"
        f"From a Basic Tier Kuudra Loot Chest:      {tentaclechance1}% or 1/{100//tentaclechance1+1}\n"
        f"From a Hot Tier Kuudra Loot Chest:        {tentaclechance2}% or 1/{100//tentaclechance2+1}\n"
        f"From a Burning Tier Kuudra Loot Chest:    {tentaclechance3}% or 1/{100//tentaclechance3+1}\n"
        f"From a Fiery Tier Kuudra Loot Chest:      {tentaclechance4}% or 1/{100//tentaclechance4+1}\n"
        f"From an Infernal Tier Kuudra Loot Chest:  {tentaclechance5}% or 1/{100//tentaclechance5+1}\n")



#treasure
treasurechance1=(0.0001*bucketmultiplier*vincentmultiplier)
treasurechance2=(0.001*bucketmultiplier*vincentmultiplier)
treasurechance3=(0.01*bucketmultiplier*vincentmultiplier)

if dye=="treasure":
    print("\nChance for Treasure Dye:\n"
        f"From a Good Catch:            {treasurechance1}% or 1/{100//treasurechance1+1}\n"
        f"From a Great Catch:           {treasurechance2}% or 1/{100//treasurechance2+1}\n"
        f"From an Outstanding Catch:    {treasurechance3}% or 1/{100//treasurechance3+1}\n")



#wild strawberry
wildstrawberrychance=(0.000000667*bucketmultiplier*vincentmultiplier)

if dye=="wild strawberry":
    print("\nChance for Wild Strawberry Dye:\n"
        f"From Harvesting a Crop: {wildstrawberrychance}% or 1/{100//wildstrawberrychance+1}\n")



#close program
input('Press Enter to exit. ')