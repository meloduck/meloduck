#dye calculator
    #a handy thingy to calculate your dye chances
    #info is mainly pulled from The Official Hypixel Skyblock Wiki and the Hypixel Skyblock Dyes discrod server
    #please note that very little is known about the order of calculations of the various items/stats that affect the chance of dye drops    
    #the order I'm currently using: RNG-Meter, Bucket of Dye, Vincent, Looting, (Legion,) Magic Find/Farming Fortune,
    #this calculator is now relatively close to being finished



#to do:
    #make legion functional
    #make farming fortune functional
    #make rng meter functional



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

#rng meter list
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



#input dye
while True:
    dye=input("Which dye would you like to select?: ")
    if dye not in dyes:
        print("That dye doesn't exist!")
    else:
        break



#input rng meter
rngmeter=False
rngmeteramount=0
rngmultiplier=1
if dye in rngList:
    while True:
        rngmeter=input("Do you have this Dye selected on your RNG-Meter? (yes/no): ")
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



#input vincent boost
vincentmultiplier=1
while True:
    boost=input("Is this Dye currently being boosted by Vincent? (yes/no): ")
    if boost=="yes":
        while True:
            vincentmultiplierinput=input("By how much? (...x): ")
            if vincentmultiplierinput=="2x"or"2":
                vincentmultiplier=2
                break
            elif vincentmultiplierinput=="3x"or"3":
                vincentmultiplier=3
                break
            else:
                print("Invalid input!")
        break
    elif boost=="no":
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
if magicfindaffected==True:
    while True:
        magicfind=int(input("How much Magic Find do you have?: "))
        if magicfind>=0:
            break
        elif magicfind<0:
            print("You can't have negative Magic Find!")
mfmultiplier={1+magicfind/100}

#input farming fortune
farmingfortune=0
if farmingfortuneaffected==True:
    while True:
        farmingfortune=int(input("How much Farming Fortune do you have?: "))
        if farmingfortune>=0:
            break
        elif magicfind<0:
            print("You can't have negative Farming Fortune!")
ffmultiplier={1} #!!!!!!!!!!!!!

#input legion level
legionlevel=0
legionamount=0
lootinglevel=0
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
    while True:
        lootinglevel=int(input("What level of looting do you have?: "))
        if lootinglevel<0:
            print("You can't have a negative level of Looting!")
        elif lootinglevel>5:
            print("You can't have a Looting level higher than 5!")
        else:
            break
legionmultiplier={1} #!!!!!!!!!!!!!!!!
lootingmultiplier={1+lootinglevel*0.15}

#input bucket of dye
bucketmultiplier=1
while True:
    bucketofdye=input("Do you have a Bucket Of Dye? (yes/no): ")
    if bucketofdye=="yes":
        bucketmultiplier=1.01
        break
    elif bucketofdye=="no":
        break
    else:
        print("Please say 'yes' or 'no'!")



print(f"\ndye: {dye}")
if rngmeter=="yes":
    print(f"rng meter: {rngmeter}")
    print(f"XP: {rngmeteramount}")
print(f"boosted: {boost}")
if boost=="yes":
    print(f"by: {vincentmultiplierinput}")
if magicfindaffected==True:
    print(
        f"magic find: {magicfind}\n"
        f"legion level: {legionlevel}\n"
        f"legion amount: {legionamount}")
if farmingfortuneaffected==True:
    print(f"farming fortune: {farmingfortune}")
if magicfindaffected==True:
    print(f"looting level: {lootinglevel}")
print(f"bucket: {bucketofdye}\n\n")



#dye chance calculations

#aquamarine FINISHED?
aquamarinechance1={0.00002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
aquamarinechance2={0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
aquamarinechance3={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="aquamarine":
    print("Chance for Aquamarine Dye:\n"
        f"From Common/Uncommon Water Sea Creatures: {aquamarinechance1}% or 1/{100//aquamarinechance1+1}\n"
        f"From Rare/Epic Water Sea Creatures: {aquamarinechance2}% or 1/{100//aquamarinechance2+1}\n"
        f"From Legendary/Mythic Water Sea Creatures: {aquamarinechance3}% or 1/{100//aquamarinechance3+1}\n")



#archfiend
archfiendchance1={0.015*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
archfiendchance2={0.15*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="archfiend":
    print("Chance for Archfiend Dye:\n"
        f"From Archfiend Dice: {archfiendchance1}% or 1/{100//archfiendchance1+1}\n"
        f"From High Class Archfiend Dice: {archfiendchance2}% or 1/{100//archfiendchance2+1}\n")



#bone FINISHED?
bonechance={0.0000333*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="bone":
    print("Chance for Bone Dye:\n"
          f"From any skeletal mob: {bonechance}% or 1/{100//bonechance+1}\n")



#brick red
brickredchance1=0.00001
brickredchance2=0.00004
brickredchance3=0.0001
brickredchance4=0.0002

if dye=="brick red":
    print("Chance for Brick Red Dye:\n"
          f"From Tier 1 Tarantula Broodfather: {brickredchance1}% or 1/{100//brickredchance1+1}\n"
          f"From Tier 2 Tarantula Broodfather: {brickredchance2}% or 1/{100//brickredchance2+1}\n"
          f"From Tier 3 Tarantula Broodfather: {brickredchance3}% or 1/{100//brickredchance3+1}\n"
          f"From Tier 4 Tarantula Broodfather: {brickredchance4}% or 1/{100//brickredchance4+1}\n")



#byzantium
byzantiumchance1=0.00001
byzantiumchance2=0.00004
byzantiumchance3=0.0001
byzantiumchance4=0.0002

if dye=="byzantium":
    print("Chance for Byzantium Dye:\n"
        f"From Tier 1 Voidgloom Seraph: {byzantiumchance1}% or 1/{100//byzantiumchance1+1}\n"
        f"From Tier 2 Voidgloom Seraph: {byzantiumchance2}% or 1/{100//byzantiumchance2+1}\n"
        f"From Tier 3 Voidgloom Seraph: {byzantiumchance3}% or 1/{100//byzantiumchance3+1}\n"
        f"From Tier 4 Voidgloom Seraph: {byzantiumchance4}% or 1/{100//byzantiumchance4+1}\n")



#carmine FINISHED?
carminechance1={0.00002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
carminechance2={0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
carminechance3={0.002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="carmine":
    print("Chance for Carmine Dye:\n"
          f"From Common/Uncommon Lava Sea Creatures: {carminechance1}% or 1/{100//carminechance1+1}\n"
          f"From Rare/Epic Lava Sea Creatures: {carminechance2}% or 1/{100//carminechance2+1}\n"
          f"From Legendary/Mythic Lava Sea Creatures: {carminechance3}% or 1/{100//carminechance3+1}\n")



#celadon
celadonchance1={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
celadonchance2={0.01*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="celadon":
    print("Chance for Celadon Dye:\n"
          f"From Blobbercyst: {celadonchance1}% or 1/{100//celadonchance1+1}\n"
          f"From Bacte: {celadonchance2}% or 1/{100//celadonchance2+1}\n")



#celeste
celestechance1={0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
celestechance2={0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
celestechance3={0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
celestechance4={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="celeste":
    print("Chance for Celeste Dye:\n"
        f"From Tier 1 Sven Packmaster: {celestechance1}% or 1/{100//celestechance1+1}\n"
        f"From Tier 2 Sven Packmaster: {celestechance2}% or 1/{100//celestechance2+1}\n"
        f"From Tier 3 Sven Packmaster: {celestechance3}% or 1/{100//celestechance3+1}\n"
        f"From Tier 4 Sven Packmaster: {celestechance4}% or 1/{100//celestechance4+1}\n")



#copper
copperchance1={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
copperchance2={0.002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
copperchance3={0.004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
copperchance4={0.02*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
copperchance5={0.2*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="copper":
    print("Chance for Copper Dye:\n"
          f"From Uncommon Visitor: {copperchance1}% or 1/{100//copperchance1+1}\n"
          f"From Rare Visitor: {copperchance2}% or 1/{100//copperchance2+1}\n"
          f"From Legendary Visitor: {copperchance3}% or 1/{100//copperchance3+1}\n"
          f"From Mythic Visitor: {copperchance4}% or 1/{100//copperchance4+1}\n"
          f"From Special Visitor: {copperchance5}% or 1/{100//copperchance5+1}\n")



#cyclamen
cyclamenchance1={0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
cyclamenchance2={0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
cyclamenchance3={0.0004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="cyclamen":
    print("Chance for Cyclamen Dye:\n\n"
        f"From:\nBezal,/nBlaze,\nFlaming Spider,\nFlare,\nKada Knight,\nMagma Cube,\nMagma Cube Rider,\nMushroom Bull,\nMutated Blaze,\nWither Skeleton,\nWither Spectre:\n{cyclamenchance1}% or 1/{100//cyclamenchance1+1}\n\n"
        f"From:\nBarbarian,\nBarbarian Gaurd,\nDive Ghast,\nFire Mage,\nGhast,\nGoliath Barbarian,\nKrondor Necromancer,\nMage Gaurd,\nMagma Glare,\nMatcho,\nMillenia-Aged Blaze,\nSmoldering Blaze,\nUnstable Magma:\n{cyclamenchance2}% or 1/{100//cyclamenchance2+1}\n\n"
        f"From:\nAshfang,\nBarbarian Duke X,\nBladesoul,\nCinderbat,\nHellwisp,\nMage Outlaw,\nMagma Boss,\nVanquisher:\n{cyclamenchance3}% or 1/{100//cyclamenchance3+1}\n")



#dark purple
darkpurplechance={0.748*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="dark purple":
    print("Chance for Dark Purple Dye:\n"
        f"To appear in a Dark(er) Auction lobby: {darkpurplechance}% or 1/{100//darkpurplechance+1}\n")



#dung
dungchance={0.0004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="dung":
    print("Chance for Dung Dye:\n"
        f"From any Pest: {dungchance}% or 1/{100//dungchance+1}")



#emerald
emeraldchance={0.00002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="emnerald":
    print("Chance for Emerald Dye:\n"
        f"Per Emerald (Ore) broken: {emeraldchance}% or 1/{100//emeraldchance+1}\n")



#flame
flamechance1={0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
flamechance2={0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
flamechance3={0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
flamechance4={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="flame":
    print("Chance for Flame Dye:\n"
        f"From Tier 1 Inferno Demonlord: {flamechance1}% or 1/{100//flamechance1+1}\n"
        f"From Tier 2 Inferno Demonlord: {flamechance2}% or 1/{100//flamechance2+1}\n"
        f"From Tier 3 Inferno Demonlord: {flamechance3}% or 1/{100//flamechance3+1}\n"
        f"From Tier 4 Inferno Demonlord: {flamechance4}% or 1/{100//flamechance4+1}\n")



#fossil
fossilchance={0.00002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="fossil":
    print("Chance for Fossil Dye to appear:\n"
        f"In Fossil Excavator: {fossilchance}% or 1/{100//fossilchance+1}\n")



#frostbitten
frostbittenchance1={0.0004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
frostbittenchance2={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
frostbittenchance3={0.01*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="frostbitten":
    print("Chance for Frostbitten Dye:\n"
        f"From Lapis Corpse: {frostbittenchance1}% or 1/{100//frostbittenchance1+1}\n"
        f"From Umber/Tungsten Corpse: {frostbittenchance2}% or 1/{100//frostbittenchance2+1}\n"
        f"From Vangaurd Corpse: {frostbittenchance3}% or 1/{100//frostbittenchance3+1}\n")



#holly
hollychance={0.00125*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="holly":
    print("Chance for Holly Dye:\n"
        f"From Red Gift: {hollychance}% or 1/{100//hollychance+1}\n")



#iceberg
icerbergchance1={0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
icerbergchance2={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
icerbergchance3={0.002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="icerberg":
    print("Chance for Icerberg Dye:\n\n"
        f"From:\nFrosty,\nFrozen Steve:\n{icerbergchance1}% or 1/{100//icerbergchance1+1}\n\n"
        f"From:\nNutcracker:\n{icerbergchance2}% or 1/{100//icerbergchance2+1}\n\n"
        f"From:\nYeti:{icerbergchance3}% or 1/{100//icerbergchance3+1}\n")



#jade
jadechance={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="jade":
    print("Chance for Jade Dye:\n"
        f"Per item roll in a Crystal Nucleus Bundle: {jadechance}% or 1/{100//jadechance+1}\n")



#livid
lividchance={0.02*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="livid":
    print("Chance for Livid Dye:\n"
        f"From Bedrock Chest in Master Catacombs Floor V {lividchance}% or 1/{100//lividchance+1}\n")



#mango
mangochance={0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="mango":
    print("Chance for Mango Dye:\n"
          f"From breaking any log: {mangochance}% or 1/{100//mangochance+1}\n")



#matcha
matchachance1={0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
matchachance2={0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
matchachance3={0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
matchachance4={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
matchachance5={0.0004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="matcha":
    print("Chance for Matcha Dye:\n"
        f"From Tier 1 Revenant Horror: {matchachance1}% or 1/{100//matchachance1+1}\n"
        f"From Tier 2 Revenant Horror: {matchachance2}% or 1/{100//matchachance2+1}\n"
        f"From Tier 3 Revenant Horror: {matchachance3}% or 1/{100//matchachance3+1}\n"
        f"From Tier 4 Revenant Horror: {matchachance4}% or 1/{100//matchachance4+1}\n"
        f"From Tier 5 Revenant Horror: {matchachance5}% or 1/{100//matchachance5+1}\n")



#midnight
midnightchance1={0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
midnightchance2={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
midnightchance3={0.002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="midnight":
    print("Chance for Midnight Dye:\n\n"
        f"From:\nCrazy Witch,\nPhantom Spirit,\nScary Jerry,\nTrick or Treater,\nWither Gourd,\nWraith:\n{midnightchance1}% or 1/{100//midnightchance1+1}\n\n"
        f"From:\nNightmare,\nScarecrow,\nWerewolf:\n{midnightchance2}% or 1/{100//midnightchance2+1}\n\n"
        f"From:\nGrim Reaper,\nHeadless Horseman,\nPhantom Fisher:\n{midnightchance3}% or 1/{100//midnightchance3+1}\n")



#mocha
mochachance1={0.000001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
mochachance2={0.00002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
mochachance3={0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
mochachance4={0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
mochachance5={0.00013*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
mochachance6={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
mochachance7={0.0004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
mochachance8={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="mocha":
    print("Chance for Mocha Dye:\n"
        f"From Level 1 Potions: {mochachance1}% or 1/{100//mochachance1+1}\n"
        f"From Level 2 Potions: {mochachance2}% or 1/{100//mochachance2+1}\n"
        f"From Level 3 Potions: {mochachance3}% or 1/{100//mochachance3+1}\n"
        f"From Level 4 Potions: {mochachance4}% or 1/{100//mochachance4+1}\n"
        f"From Level 5 Potions: {mochachance5}% or 1/{100//mochachance5+1}\n"
        f"From Level 6 Potions: {mochachance6}% or 1/{100//mochachance6+1}\n"
        f"From Level 7 Potions: {mochachance7}% or 1/{100//mochachance7+1}\n"
        f"From Level 8 Potions: {mochachance8}% or 1/{100//mochachance8+1}\n")



#nadeshiko
nadeshikochance1={0.00133*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
nadeshikochance2={0.002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
nadeshikochance3={0.004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="nadeshiko":
    print("Chance for Nadeshiko Dye to appear:\n"
        f"In Supreme Superpairs Experiment: {nadeshikochance1}% or 1/{100//nadeshikochance1+1}\n"
        f"In Transcendent Superpairs Experiment: {nadeshikochance2}% or 1/{100//nadeshikochance2+1}\n"
        f"In Metaphysical Superpairs Experiment: {nadeshikochance3}% or 1/{100//nadeshikochance3+1}\n")



#necron
necronchance={0.04*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="necron":
    print("Chance for Necron Dye:\n"
        f"From Bedrock Chest in Master Catacombs Floor VII: {necronchance}% or 1/{100//necronchance+1}\n")



#nyanza
nyanzachance={0.0004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="nyanza":
    print("Chance for Nyanza Dye:\n"
        f"From completing a Commission: {nyanzachance}% or 1/{100//nyanzachance+1}\n")



#pearlescent
pearlescentchance1={0.00001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
pearlescentchance2={0.00002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
pearlescentchance3={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
pearlescentchance4={0.002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="pearlescent":
    print("Chance for Pearlescent Dye:\n\n"
        f"From:\nEnderman,\nEndermite,\nObsidiant Defender,\nSeer,\nZealot,\nZealot Bruiser:\n{pearlescentchance1}% or 1/{100//pearlescentchance1+1}\n\n"
        f"From:\nNest Endermite,\nVoidling Extremist,\nVoidling Fenatic:\n{pearlescentchance2}% or 1/{100//pearlescentchance2+1}\n\n"
        f"From:\nEnd Stone Protector,\nOld Dragon,\nProtector Dragon,\nSpecial Zealot,\nStrong Dragon,\nUnstable Dragon,\nWise Dragon,\nYoung Dragon:\n{pearlescentchance3}% or 1/{100//pearlescentchance3+1}\n\n"
        f"From:\nSuperior Dragon:\n{pearlescentchance4}% or 1/{100//pearlescentchance4+1}\n")



#pelt
peltchance1={0.0004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
peltchance2={0.0005*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
peltchance3={0.000667*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
peltchance4={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
peltchance5={0.01*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="pelt":
    print("Chance for Pelt Dye:\n"
        f"From a Trackable Animal: {peltchance1}% or 1/{100//peltchance1+1}\n"
        f"From an Untrackable Animal: {peltchance2}% or 1/{100//peltchance2+1}\n"
        f"From an Undetected Animal: {peltchance3}% or 1/{100//peltchance3+1}\n"
        f"From an Endangered Animal: {peltchance4}% or 1/{100//peltchance4+1}\n"
        f"From an Elusive Animal: {peltchance5}% or 1/{100//peltchance5+1}\n")



#periwinkle
periwinklechance1={0.0002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
periwinklechance2={0.00025*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
periwinklechance3={0.000333*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
periwinklechance4={0.0005*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
periwinklechance5={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="periwinkle":
    print("Chance for Periwinkle Dye:\n"
        f"From Level 1-99 Runic Mobs: {periwinklechance1}% or 1/{100//periwinklechance1+1}\n"
        f"From Level 100-199 Runic Mobs: {periwinklechance2}% or 1/{100//periwinklechance2+1}\n"
        f"From Level 200-299 Runic Mobs: {periwinklechance3}% or 1/{100//periwinklechance3+1}\n"
        f"From Level 300-399 Runic Mobs: {periwinklechance4}% or 1/{100//periwinklechance4+1}\n"
        f"From level 400+ Runic Mobs: {periwinklechance5}% or 1/{100//periwinklechance5+1}\n")



#sangria
sangriachance1={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
sangriachance2={0.00125*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
sangriachance3={0.00167*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
sangriachance4={0.0025*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
sangriachance5={0.01*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="sangria":
    print("Chance for Sangria Dye:\n"
        f"From Tier 1 Riftstalker Bloodfiend: {sangriachance1}% or 1/{100//sangriachance1+1}\n"
        f"From Tier 2 Riftstalker Bloodfiend: {sangriachance2}% or 1/{100//sangriachance2+1}\n"
        f"From Toer 3 Riftstalker Bloodfiend: {sangriachance3}% or 1/{100//sangriachance3+1}\n"
        f"From Tier 4 Riftstalker BloodfiendL {sangriachance4}% or 1/{100//sangriachance4+1}\n"
        f"From Tier 5 Riftstalker Bloodfiend: {sangriachance5}% or 1/{100//sangriachance5+1}\n")



#secret
secretchance={0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="secret":
    print("Chance for Secret Dye:\n"
        f"From Collecting a Secret: {secretchance}% or 1/{100//secretchance+1}\n")



#tentacle
tentaclechance1={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
tentaclechance2={0.00125*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
tentaclechance3={0.00167*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
tentaclechance4={0.0025*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
tentaclechance5={0.005*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="tentactle":
    print("Chance for Tentacle Dye:\n"
        f"From a Basic Tier Kuudra Loot Chest: {tentaclechance1}% or 1/{100//tentaclechance1+1}\n"
        f"From a Hot Tier Kuudra Loot Chest: {tentaclechance2}% or 1/{100//tentaclechance2+1}\n"
        f"From a Burning Tier Kuudra Loot Chest: {tentaclechance3}% or 1/{100//tentaclechance3+1}\n"
        f"From a Fiery Tier Kuudra Loot Chest: {tentaclechance4}% or 1/{100//tentaclechance4+1}\n"
        f"From an Infernal Tier Kuudra Loot Chest: {tentaclechance5}% or 1/{100//tentaclechance5+1}\n")



#treasure
treasurechance1={0.0001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
treasurechance2={0.001*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}
treasurechance3={0.01*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="treasure":
    print("Chance for Treasure Dye:\n"
        f"From a Good Catch: {treasurechance1}% or 1/{100//treasurechance1+1}\n"
        f"From a Great Catch: {treasurechance2}% or 1/{100//treasurechance2+1}\n"
        f"From an Outstanding Catch: {treasurechance3}% or 1/{100//treasurechance3+1}\n")



#wild strawberry
wildstrawberrychance={0.000000667*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier*ffmultiplier}

if dye=="wild strawberry":
    print("Chance for Wild Strawberry Dye:\n"
        f"From Harvesting a Crop: {wildstrawberrychance}% or 1/{100//wildstrawberrychance+1}\n")