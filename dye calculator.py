#dye calculator
    #a handy thingy to calculate your dye chances

#to do
    #input conditions of all dyes(affected by)
    #input chances of all dyes
    #

#dyeList
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



#input dye
while True:
    dye=input("Which dye would you like to select?: ")
    if dye not in dyes:
        print("That dye doesn't exist!")
    else:
        break



#is the dye affected by magic find?
magicfindaffected=False
if dye=="carmine":
    magicfindaffected=True

#is the dye affected by farming fortune?
farmingfortuneaffected=False
if dye=="dung":
    farmingfortuneaffected=True

#is the dye affected by looting?
lootingaffected=False 
if dye=="pearlescent":
    lootingaffected=True



#input magic find
if magicfindaffected==True:
    while True:
        magicfind=int(input("How much Magic Find do you have?: "))
        if magicfind>=0:
            break
        elif magicfind<0:
            print("You can't have negative Magic Find!")

#input farming fortune
if farmingfortuneaffected==True:
    while True:
        farmingfortune=int(input("How much Farming Fortune do you have?: "))
        if farmingfortune>=0:
            break
        elif magicfind<0:
            print("You can't have negative Farming Fortune!")

#input legion level
if magicfindaffected==True:
    while True:
        legionlevel=int(input("What level of Legion do you have?: "))
        if legionlevel<0:
            print("You can't have a negative level of Legion!")
        elif legionlevel>20:
            print("You can't have a Legion level higher than 20!")
        else:
            break

    #input amount of people close 
    while True:
        legionamount=int(input("How many people are close to you?: "))
        if legionamount<0:
            print("There can't be negative people close to you!")
        elif legionamount>20:
            legionamount=20
            break
        else:
            break

#input looting level
if lootingaffected==True:
    while True:
        lootinglevel=int(input("What level of looting do you have?: "))
        if lootinglevel<0:
            print("You can't have a negative level of Looting!")
        elif lootinglevel>5:
            print("You can't have a Looting level higher than 5!")
        else:
            break

#input bucket of dye
while True:
    bucketofdye=input("Do you have a Bucket Of Dye (yes/no)?: ")
    if bucketofdye!="yes" and bucketofdye!="no":
        print("Invalid input")
    else:
        break


print(f"\ndye: {dye}")
if magicfindaffected==True:
    print(
        f"magic find: {magicfind}\n"
        f"legion level: {legionlevel}\n"
        f"legion amount: {legionamount}")
if farmingfortuneaffected==True:
    print(
        f"farming fortune: {farmingfortune}")
if lootingaffected==True:
    print(
        f"looting level: {lootinglevel}")
print(f"bucket: {bucketofdye}\n")



#aquamarine
aquamarinechance1=0.00002
aquamarinechance2=0.00004
aquamarinechance3=0.0002
if dye=="aquamarine":
    print(
        f"From Common/Uncommon sea creatures: {aquamarinechance1}\n"
        f"From Rare/Epic sea creatures: {aquamarinechance2}\n"
        f"From Legendary/Mythic sea creatures: {aquamarinechance3}\n")



#archfiend
archfiendchance1=0.015
archfiendchance2=0.15



#bone
bonechance=0.0000333



#brick red
brickredchance1=0.00001
brickredchance2=0.00004
brickredchance3=0.0001
brickredchance4=0.0002



#byzantium
byzantiumchance1=0.00001
byzantiumchance2=0.00004
byzantiumchance3=0.0001
byzantiumchance4=0.0002



#carmine
carminechance1=0.00002
carminechance2=0.00004
carminechance3=0.002



#celadon
