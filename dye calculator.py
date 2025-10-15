#dye calculator
    #a handy thingy to calculate your dye chances
    #please note that most if not all of the drop chance information is pulled from The Official Hypixel Skyblock Wiki

#to do
    #input conditions of all dyes(affected by)
    #input chances of all dyes
    #add vincent buffs
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
    print("Chance for Aquamarine Dye:\n"
        f"From Common/Uncommon Water Sea Creatures: {aquamarinechance1}%\n"
        f"From Rare/Epic Water Sea Creatures: {aquamarinechance2}%\n"
        f"From Legendary/Mythic Water Sea Creatures: {aquamarinechance3}%\n")



#archfiend
archfiendchance1=0.015
archfiendchance2=0.15

if dye=="archfiend":
    print("Chance for Archfiend Dye:\n"
        f"From Archfiend Dice: {archfiendchance1}%\n"
        f"From High Class Archfiend Dice: {archfiendchance2}%\n")



#bone
bonechance=0.0000333

if dye=="bone":
    print("Chance for Bone Dye:\n"
          f"From any skeletal mob: {bonechance}%\n")



#brick red
brickredchance1=0.00001
brickredchance2=0.00004
brickredchance3=0.0001
brickredchance4=0.0002

if dye=="brick red":
    print("Chance for Brick Red Dye:\n"
          f"From Tier 1 Tarantula Broodfather: {brickredchance1}%\n"
          f"From Tier 2 Tarantula Broodfather: {brickredchance2}%\n"
          f"From Tier 3 Tarantula Broodfather: {brickredchance3}%\n"
          f"From Tier 4 Tarantula Broodfather: {brickredchance4}%\n")



#byzantium
byzantiumchance1=0.00001
byzantiumchance2=0.00004
byzantiumchance3=0.0001
byzantiumchance4=0.0002

if dye=="byzantium":
    print("Chance for Byzantium Dye:\n"
        f"From Tier 1 Voidgloom Seraph: {byzantiumchance1}%\n"
        f"From Tier 2 Voidgloom Seraph: {byzantiumchance2}%\n"
        f"From Tier 3 Voidgloom Seraph: {byzantiumchance3}%\n"
        f"From Tier 4 Voidgloom Seraph: {byzantiumchance4}%\n")



#carmine
carminechance1=0.00002
carminechance2=0.00004
carminechance3=0.002

if dye=="carmine":
    print("Chance for Carmine Dye:\n"
          f"From Common/Uncommon Lava Sea Creatures: {carminechance1}%\n"
          f"From Rare/Epic Lava Sea Creatures: {carminechance2}%\n"
          f"From Legendary/Mythic Lava Sea Creatures: {carminechance3}%\n")



#celadon
celadonchance1=0.001
celadonchance2=0.01

if dye=="celadon":
    print("Chance for Celadon Dye:\n"
          f"From Blobbercyst: {celadonchance1}%\n"
          f"From Bacte: {celadonchance2}%\n")



#celeste
celestechance1=0.00001
celestechance2=0.00004
celestechance3=0.0001
celestechance4=0.0002

if dye=="celeste":
    print("Chance for Celeste Dye:\n"
        f"From Tier 1 Sven Packmaster: {celestechance1}%\n"
        f"From Tier 2 Sven Packmaster: {celestechance2}%\n"
        f"From Tier 3 Sven Packmaster: {celestechance3}%\n"
        f"From Tier 4 Sven Packmaster: {celestechance4}%\n")



#copper
copperchance1=0.001
copperchance2=0.002
copperchance3=0.004
copperchance4=0.02
copperchance5=0.2

if dye=="copper":
    print("Chance for Copper Dye:\n"
          f"From Uncommon Visitor: {copperchance1}%\n"
          f"From Rare Visitor: {copperchance2}%\n"
          f"From Legendary Visitor: {copperchance3}%\n"
          f"From Mythic Visitor: {copperchance4}%\n"
          f"From Special Visitor: {copperchance5}%\n")



#cyclamen
cyclamenchance1=0.00001
cyclamenchance2=0.00004
cyclamenchance3=0.0004

if dye=="cyclamen":
    print("Chance for Cyclamen Dye:\n\n"
        f"From:\nBezal,/nBlaze,\nFlaming Spider,\nFlare,\nKada Knight,\nMagma Cube,\nMagma Cube Rider,\nMushroom Bull,\nMutated Blaze,\nWither Skeleton,\nWither Spectre:\n{cyclamenchance1}%\n\n"
        f"From:\nBarbarian,\nBarbarian Gaurd,\nDive Ghast,\nFire Mage,\nGhast,\nGoliath Barbarian,\nKrondor Necromancer,\nMage Gaurd,\nMagma Glare,\nMatcho,\nMillenia-Aged Blaze,\nSmoldering Blaze,\nUnstable Magma:\n{cyclamenchance2}%\n\n"
        f"From:\nAshgang,\nBarbarian Duke X,\nBladesoul,\nCinderbat,\nHellwisp,\nMage Outlaw,\nMagma Boss,\nVanquisher:\n{cyclamenchance3}%\n")



#dark purple
darkpurplechance=0.748

if dye=="dark purple":
    print("Chance for Dark Purple Dye:\n"
        f"For each Dark Auction lobby the chance for it to appear is {darkpurplechance}%\n")



#dung
dungchance=0.0004

if dye=="dung":
    print("Chance for Dung Dye:\n"
        f"From any Pest: {dungchance}%")



#emerald
emeraldchance=0.00002

if dye=="emnerald":
    print("Chance for Emerald Dye:\n"
        f"From (Pure) Emerald: {emeraldchance}%\n")



#flame
flamechance1=0.00001
flamechance2=0.00004
flamechance3=0.0001
flamechance4=0.0002

if dye=="flame":
    print("Chance for Flame Dye:\n"
        f"From Tier 1 Inferno Demonlord: {flamechance1}%\n"
        f"From Tier 2 Inferno Demonlord: {flamechance2}%\n"
        f"From Tier 3 Inferno Demonlord: {flamechance3}%\n"
        f"From Tier 4 Inferno Demonlord: {flamechance4}%\n")



#fossil
fossilchance=0.00002

if dye=="fossil":
    print("Chance for Fossil Dye to appear:\n"
        f"In Fossil Excavator: {fossilchance}%\n")



#frostbitten
frostbittenchance1=0.0004
frostbittenchance2=0.001
frostbittenchance3=0.01

if dye=="frostbitten":
    print("Chance for Frostbitten Dye:\n"
        f"From Lapis Corpse: {frostbittenchance1}%\n"
        f"From Umber/Tungsten Corpse: {frostbittenchance2}%\n"
        f"From Vangaurd Corpse: {frostbittenchance3}%\n")



#holly
hollychance=0.00125

if dye=="holly":
    print("Chance for Holly Dye:\n"
        f"From Red Gift: {hollychance}%\n")



#iceberg
icerbergchance1=0.0001
icerbergchance2=0.0002
icerbergchance3=0.002

if dye=="icerberg":
    print("Chance for Icerberg Dye:\n\n"
        f"From:\nFrosty,\nFrozen Steve:\n{icerbergchance1}%\n\n"
        f"From:\nGrinch,\nNutcracker:\n{icerbergchance2}%\n\n"
        f"From:\nReindrake,\nYeti:{icerbergchance3}%\n")



#jade
jadechance=0.0002

if dye=="jade":
    print("Chance for Jade Dye\n"
        f"Per item roll in a Crystal Nucleus Bundle: {jadechance}%\n")



#livid
lividchance=0.02

if dye=="livid":
    print("Chance for Livid Dye\n"
        f"From Bedrock Chest in Master Catacombs Floor V {lividchance}%\n")



#mango
mangochance=0.00001

if dye=="mango":
    print("Chance for Mango Dye\n"
          f"From breaking any log: {mangochance}%\n")



#matcha
matchachance1=0.00001
matchachance2=0.00004
matchachance3=0.0001
matchachance4=0.0002
matchachance5=0.0004

if dye=="matcha":
    print("Chance for Matcha Dye\n"
        f"From Tier 1 Revenant Horror: {matchachance1}%\n"
        f"From Tier 2 Revenant Horror: {matchachance2}%\n"
        f"From Tier 3 Revenant Horror: {matchachance3}%\n"
        f"From Tier 4 Revenant Horror: {matchachance4}%\n"
        f"From Tier 5 Revenant Horror: {matchachance5}%\n")



#midnight
midnightchance1=0.0001
midnightchance2=0.0002
midnightchance3=0.002

if dye=="midnight":
    print("Chance for Midnight Dye:\n\n"
        f"From:\nCrazy Witch,\nPhantom Spirit,\nScary Jerry,\nTrick or Treater,\nWither Gourd,\nWraith:\n{midnightchance1}%\n\n"
        f"From:\nNightmare,\nScarecrow,\nWerewolf:\n{midnightchance2}%\n\n"
        f"From:\nGrim Reaper,\nHeadless Horseman,\nPhantom Fisher:\n{midnightchance3}%\n")



#mocha
mochachance1=0.000001
mochachance2=0.00002
mochachance3=0.00004
mochachance4=0.0001
mochachance5=0.00013
mochachance6=0.0002
mochachance7=0.0004
mochachance8=0.001

if dye=="mocha":
    print("Chance for Mocha Dye:\n"
        f"From Level 1 Potions: {mochachance1}%\n"
        f"From Level 2 Potions: {mochachance2}%\n"
        f"From Level 3 Potions: {mochachance3}%\n"
        f"From Level 4 Potions: {mochachance4}%\n"
        f"From Level 5 Potions: {mochachance5}%\n"
        f"From Level 6 Potions: {mochachance6}%\n"
        f"From Level 7 Potions: {mochachance7}%\n"
        f"From Level 8 Potions: {mochachance8}%\n")



#nadeshiko
nadeshikochance1=0.00133
nadeshikochance2=0.002
nadeshikochance3=0.004

if dye=="nadeshiko":
    print("Chance for Nadeshiko Dye to appear:\n"
        f"In Supreme Superpairs Experiment: {nadeshikochance1}%\n"
        f"In Transcendent Superpairs Experiment: {nadeshikochance2}%\n"
        f"In Metaphysical Superpairs Experiment: {nadeshikochance3}%\n")



#necron
necronchance=0.04

if dye=="necron":
    print("Chance for Necron Dye:\n"
        f"From Bedrock Chest in Master Catacombs Floor VII: {necronchance}%\n")



#nyanza
nyanzachance=0.0004

if dye=="nyanza":
    print("Chance for Nyanza Dye\n"
        f"From completing a Commission: {nyanzachance}%\n")



#pearlescent
pearlescentchance1=0.00001
pearlescentchance2=0.00002
pearlescentchance3=0.001
pearlescentchance4=0.002

if dye=="pearlescent":
    print("Chance for Pearlescent Dye:\n\n"
        f"From:\nEnderman,\nEndermite,\nObsidiant Defender,\nSeer,\nZealot,\nZealot Bruiser:\n{pearlescentchance1}%\n\n"
        f"From:\nNest Endermite,\nVoidling Extremist,\nVoidling Fenatic:\n{pearlescentchance2}%\n\n"
        f"From:\nEnd Stone Protector,\nOld Dragon,\nProtector Dragon,\nSpecial Zealot,\nStrong Dragon,\nUnstable Dragon,\nWise Dragon,\nYoung Dragon:\n{pearlescentchance3}%\n\n"
        f"From:\nSuperior Dragon:\n{pearlescentchance4}%\n")



#pelt
peltchance1=0.0004
peltchance2=0.0005
peltchance3=0.000667
peltchance4=0.001
peltchance5=0.01

if dye=="pelt":
    print("Chance for Pelt Dye:\n"
        f"From Trackable Animal: {peltchance1}%\n"
        f"From Untrackable Animal: {peltchance2}%\n"
        f"From Undetected Animal: {peltchance3}%\n"
        f"From Endangered Animal: {peltchance4}%\n"
        f"From Elusive Animal: {peltchance5}%\n")



#periwinkle
periwinklechance1=0.0002
periwinklechance2=0.00025
periwinklechance3=0.000333
periwinklechance4=0.0005
periwinklechance5=0.001

if dye=="periwinkle":
    print("Chance for Periwinkle Dye:\n"
        f"From Level 1-99 Runic Mobs: {periwinklechance1}%\n"
        f"From Level 100-199 Runic Mobs: {periwinklechance2}%\n"
        f"From Level 200-299 Runic Mobs: {periwinklechance3}%\n"
        f"From Level 300-399 Runic Mobs: {periwinklechance4}%\n"
        f"From level 400+ Runic Mobs: {periwinklechance5}%\n")



#sangria
sangriachance1=0.001
sangriachance2=0.00125
sangriachance3=0.00167
sangriachance4=0.0025
sangriachance5=0.01

if dye=="sangria":
    print("Chance for Sangria Dye:\n"
        f"From Tier 1 Riftstalker Bloodfiend: {sangriachance1}%\n"
        f"From Tier 2 Riftstalker Bloodfiend: {sangriachance2}%\n"
        f"From Toer 3 Riftstalker Bloodfiend: {sangriachance3}%\n"
        f"From Tier 4 Riftstalker BloodfiendL {sangriachance4}%\n"
        f"From Tier 5 Riftstalker Bloodfiend: {sangriachance5}%\n")



#secret
secretchance=0.0001

if dye=="secret":
    print("Chance for Secret Dye:\n"
        f"From Collecting a Secret: {secretchance}%\n")



#tentacle
tentaclechance1=0.001
tentaclechance2=0.00125
tentaclechance3=0.00167
tentaclechance4=0.0025
tentaclechance5=0.005

if dye=="tentactle":
    print("Chance for Tentacle Dye:\n"
        f"From a Basic Tier Kuudra Loot Chest: {tentaclechance1}%\n"
        f"From a Hot Tier Kuudra Loot Chest: {tentaclechance2}%\n"
        f"From a Burning Tier Kuudra Loot Chest: {tentaclechance3}%\n"
        f"From a Fiery Tier Kuudra Loot Chest: {tentaclechance4}%\n"
        f"From an Infernal Tier Kuudra Loot Chest: {tentaclechance5}%\n")



#treasure
treasurechance1=0.0001
treasurechance2=0.001
treasurechance3=0.01

if dye=="treasure":
    print("Chance for Treasure Dye:\n"
        f"From a Good Catch: {treasurechance1}%\n"
        f"From a Great Catch: {treasurechance2}%\n"
        f"From an Outstanding Catch: {treasurechance3}%\n")



#wild strawberry
wildstrawberrychance=0.000000667

if dye=="wild strawberry:":
    print("Chance for Wild Strawberry Dye:\n"
        f"From Harvesting a Crop: {wildstrawberrychance}%\n")