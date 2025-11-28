#dye hunters
    #a handy thingy to calculate your dye chances(and maybe estimated time required to drop one in the future)
    #info is mainly pulled from The Official Hypixel Skyblock Wiki and the (unofficial) Hypixel Skyblock Dyes discord server
    #please note that very little is known about how the various items/stats/behaviours that affect the chance of dye drops work exactly, due to this anything that comes out of this calculator could not be true
    #this calculator is now relatively close to being finished



#to do:
    #add time estimates to all dyes maybe
    #look into exporting it as an exe file
    #functions!
    #add relevant attributes!
    #distribute thru different files to make finding things easier
    #TURN IT INTO A WEBSITE (options: dyehunters.com, dyeblock.com), with GUI inspired by SkyShards, made in TypeScript
    #pull vincent boost from API maybe
    #improve jade dye



#imports
from functions import input_dye
from functions import chisel_gemstone_checks
from functions import input_bucket_of_dye
from functions import input_vincent_multiplier
from functions import input_vincent_multiplier_amount
from functions import test_affected_ff
from functions import test_affected_mf
from functions import test_affected_rngmeter
from functions import test_int_cf
from functions import input_ff
from functions import input_rngmeter
from lists import all_dyes_bucketofdye_list



#input dye
dye=input_dye.getdye()

#is the dye affected by magic find (and looting)?
magicfindaffected=test_affected_mf.testmfaffected()

#is the dye affected by farming fortune?
farmingfortuneaffected=test_affected_ff.testffaffected()

#is the dye affected by RNG meter?
rngaffected=test_affected_rngmeter.testrngaffected()


#input vincent boost
#is dye boosted?
vincentboosted=input_vincent_multiplier.inputvincentboosted()
#boosted by how much?
vincentmultiplier=1
if vincentboosted==True:
    vincentmultiplier=input_vincent_multiplier_amount.inputvincentmultiplier()



#input bucket of dye
bucketmultiplier=input_bucket_of_dye.input_bucket_of_dye()
bucketofdye=input_bucket_of_dye.getbucketofdye()



#input rng meter
rngmeter=input_rngmeter.inputrngmeterselected()
rngmeteramount=input_rngmeter.getrngmeteramount()

rngmultiplier=1 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#turn rngmeteramount into float from 0.0-1.0
#then the formula is: chance=base chance*(1+2*float)



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
    if legionlevel>0:
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
    #input farming fortune and test for int, if not int return "Invalid input!" and try again
    farmingfortune=input_ff.inputff()

    #input crop fortune and test for int, if not int return "Invalid input!" and try again
    #cactus
    cactusfortune=test_int_cf.inputcf("Cactus")
    
    #carrot
    carrotfortune=test_int_cf.inputcf("Carrot")

    #cocoabeans
    cocoabeansfortune=test_int_cf.inputcf("Cocoa Beans")

    #melon
    melonfortune=test_int_cf.inputcf("Melon")

    #mushroom
    mushroomfortune=test_int_cf.inputcf("Mushroom")

    #nether wart
    netherwartfortune=test_int_cf.inputcf("Nether Wart")

    #potato
    potatofortune=test_int_cf.inputcf("Potato")

    #pumpkin
    pumpkinfortune=test_int_cf.inputcf("Pumpkin")

    #sugar cane
    sugarcanefortune=test_int_cf.inputcf("Sugar Cane")

    #wheat
    wheatfortune=test_int_cf.inputcf("Wheat")



#fossil dye inputs
chiselcharges=0
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
            chiselgemstone1type=chisel_gemstone_checks.checkgemslot1type()
            
            #1st slot tier
            chiselgemstone1tier=chisel_gemstone_checks.checkgemslot1tier()
            
        #tier 3 chisel
        elif chisel=="glacite-plated" or chisel=="glacite plated" or chisel=="glacite-plated chisel" or chisel=="glacite plated chisel" or chisel=="t3" or chisel=="3":
            #1st slot type
            chiselgemstone1type=chisel_gemstone_checks.checkgemslot1type()

            #1st slot tier
            chiselgemstone1tier=chisel_gemstone_checks.checkgemslot1tier()
            
            #2nd slot type
            chiselgemstone2type=chisel_gemstone_checks.checkgemslot2type()

            #2nd slot tier
            chiselgemstone2tier=chisel_gemstone_checks.checkgemslot2tier()

        #tier 4 chisel
        elif chisel=="perfect" or chisel=="perfect chisel" or chisel=="t4" or chisel=="4":
            #1st slot type
            chiselgemstone1type=chisel_gemstone_checks.checkgemslot1type()

            #1st slot tier
            chiselgemstone1tier=chisel_gemstone_checks.checkgemslot1tier()

            #2nd slot type
            chiselgemstone2type=chisel_gemstone_checks.checkgemslot2type()

            #2nd slot tier
            chiselgemstone2tier=chisel_gemstone_checks.checkgemslot2tier()

            #3rd slot type
            chiselgemstone3type=chisel_gemstone_checks.checkgemslot3type()

            #3rd slot tier
            chiselgemstone3tier=chisel_gemstone_checks.checkgemslot3tier()
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

#fetch chisel gemstone multipliers
aquamarinemultiplier=chisel_gemstone_checks.aquamarinemultiplier
citrinemultiplier=chisel_gemstone_checks.citrinemultiplier
onyxmultiplier=chisel_gemstone_checks.onyxmultiplier



#print info
print(f"\n\nSelected Dye: {dye}")
if rngmeter=="yes":
    print(
        f"Selected on RNG-Meter: {rngmeter}"
        f"Amount of XP in RNG-Meter: {rngmeteramount}")
print(f"Boosted by Vincent: {vincentboosted}")
if vincentboosted=="yes":
    print(f"Boosted by: {vincentmultiplier}\n\n")
if dye in all_dyes_bucketofdye_list.bucketofdyeList:
    print(f"Bucket of Dye: {bucketofdye}")
if dye=="fossil":
    print(f"Chisel tier: {chisel}\n")
    if chisel=="reinforced" or chisel=="reinforced chisel" or chisel=="t2" or chisel=="2":
        print(
            f"Gemstone type: {chiselgemstone1type}"
            f"Gemstone tier: {chiselgemstone1tier}\n")
    elif chisel=="glacite-plated" or chisel=="glacite plated" or chisel=="glacite-plated chisel" or chisel=="glacite plated chisel" or chisel=="t3" or chisel=="3":
        print(
            f"1st slot Gemstone type: {chiselgemstone1type}"
            f"1st slot Gemstone tier: {chiselgemstone1tier}\n"
            f"2nd slot Gemstone type: {chiselgemstone2type}"
            f"2nd slot Gemstone tier: {chiselgemstone2tier}\n")
    elif chisel=="perfect" or chisel=="perfect chisel" or chisel=="t4" or chisel=="4":
        print(
            f"1st slot Gemstone type: {chiselgemstone1type}"
            f"1st slot Gemstone tier: {chiselgemstone1tier}\n"
            f"2nd slot Gemstone type: {chiselgemstone2type}"
            f"2nd slot Gemstone tier: {chiselgemstone2tier}\n"
            f"3rd slot Gemstone type: {chiselgemstone3type}"
            f"3rd slot Gemstone tier: {chiselgemstone3tier}\n")
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
        f"From Common/Uncommon Water Sea Creatures:     {aquamarinechance1:f}% or 1/{100/aquamarinechance1}\n"
        f"From Rare/Epic Water Sea Creatures:           {aquamarinechance2:f}% or 1/{100/aquamarinechance2}\n"
        f"From Legendary/Mythic Water Sea Creatures:    {aquamarinechance3:f}% or 1/{100/aquamarinechance3}\n")



#archfiend
archfiendchance1=(0.015*bucketmultiplier*vincentmultiplier)
archfiendchance2=(0.15*bucketmultiplier*vincentmultiplier)

if dye=="archfiend":
    print("\nChance for Archfiend Dye:\n"
        f"From rolling an Archfiend Dice:           {archfiendchance1:f}% or 1/{100/archfiendchance1}\n"
        f"From rolling a High Class Archfiend Dice: {archfiendchance2:f}% or 1/{100/archfiendchance2}\n")



#bone
bonechance=((1/30000)*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="bone":
    print("\nChance for Bone Dye:\n"
        f"From any skeletal mob: {bonechance:f}% or 1/{100/bonechance}\n")



#brick red
brickredchance1=(0.00001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
brickredchance2=(0.00004*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
brickredchance3=(0.0001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
brickredchance4=(0.0002*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)

if dye=="brick red":
    print("\nChance for Brick Red Dye:\n"
          f"From Tier 1 Tarantula Broodfather: {brickredchance1:f}% or 1/{100/brickredchance1}\n"
          f"From Tier 2 Tarantula Broodfather: {brickredchance2:f}% or 1/{100/brickredchance2}\n"
          f"From Tier 3 Tarantula Broodfather: {brickredchance3:f}% or 1/{100/brickredchance3}\n"
          f"From Tier 4 Tarantula Broodfather: {brickredchance4:f}% or 1/{100/brickredchance4}\n")



#byzantium
byzantiumchance1=(0.00001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
byzantiumchance2=(0.00004*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
byzantiumchance3=(0.0001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
byzantiumchance4=(0.0002*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)

if dye=="byzantium":
    print("\nChance for Byzantium Dye:\n"
        f"From Tier 1 Voidgloom Seraph: {byzantiumchance1:f}% or 1/{100/byzantiumchance1}\n"
        f"From Tier 2 Voidgloom Seraph: {byzantiumchance2:f}% or 1/{100/byzantiumchance2}\n"
        f"From Tier 3 Voidgloom Seraph: {byzantiumchance3:f}% or 1/{100/byzantiumchance3}\n"
        f"From Tier 4 Voidgloom Seraph: {byzantiumchance4:f}% or 1/{100/byzantiumchance4}\n")



#carmine
carminechance1=(0.00002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
carminechance2=(0.00004*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
carminechance3=(0.002*rngmultiplier*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="carmine":
    print("\nChance for Carmine Dye:\n"
          f"From Common/Uncommon Lava Sea Creatures:    {carminechance1:f}% or 1/{100/carminechance1}\n"
          f"From Rare/Epic Lava Sea Creatures:          {carminechance2:f}% or 1/{100/carminechance2}\n"
          f"From Legendary/Mythic Lava Sea Creatures:   {carminechance3:f}% or 1/{100/carminechance3}\n")



#celadon
celadonchance1=(0.001*rngmultiplier*vincentmultiplier)
celadonchance2=(0.01*rngmultiplier*vincentmultiplier)

if dye=="celadon":
    print("\nChance for Celadon Dye:\n"
          f"From Bacte:         {celadonchance2:f}% or 1/{100/celadonchance2}\n"
          f"From Blobbercyst:   {celadonchance1:f}% or 1/{100/celadonchance1}\n")



#celeste
celestechance1=(0.00001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
celestechance2=(0.00004*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
celestechance3=(0.0001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
celestechance4=(0.0002*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)

if dye=="celeste":
    print("\nChance for Celeste Dye:\n"
        f"From Tier 1 Sven Packmaster: {celestechance1:f}% or 1/{100/celestechance1}\n"
        f"From Tier 2 Sven Packmaster: {celestechance2:f}% or 1/{100/celestechance2}\n"
        f"From Tier 3 Sven Packmaster: {celestechance3:f}% or 1/{100/celestechance3}\n"
        f"From Tier 4 Sven Packmaster: {celestechance4:f}% or 1/{100/celestechance4}\n")



#copper
copperchance1=(0.001*bucketmultiplier*vincentmultiplier)
copperchance2=(0.002*bucketmultiplier*vincentmultiplier)
copperchance3=(0.004*bucketmultiplier*vincentmultiplier)
copperchance4=(0.02*bucketmultiplier*vincentmultiplier)
copperchance5=(0.2*bucketmultiplier*vincentmultiplier)

if dye=="copper":
    print("\nChance for Copper Dye:\n"
          f"From Uncommon Visitor:  {copperchance1:f}% or 1/{100/copperchance1}\n"
          f"From Rare Visitor:      {copperchance2:f}% or 1/{100/copperchance2}\n"
          f"From Legendary Visitor: {copperchance3:f}% or 1/{100/copperchance3}\n"
          f"From Mythic Visitor:    {copperchance4:f}% or 1/{100/copperchance4}\n"
          f"From Special Visitor:   {copperchance5:f}% or 1/{100/copperchance5}\n")



#cyclamen
cyclamenchance1=(0.00001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
cyclamenchance2=(0.00004*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
cyclamenchance3=(0.0004*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="cyclamen":
    print("\nChance for Cyclamen Dye:\n\n"
        f"From:\nBezal,\nBlaze,\nFlaming Spider,\nFlare,\nKada Knight,\nMagma Cube,\nMagma Cube Rider,\nMushroom Bull,\nMutated Blaze,\nWither Skeleton,\nWither Spectre:\n{cyclamenchance1:f}% or 1/{100/cyclamenchance1}\n\n"
        f"From:\nBarbarian,\nBarbarian Gaurd,\nDive Ghast,\nFire Mage,\nGhast,\nGoliath Barbarian,\nKrondor Necromancer,\nMage Gaurd,\nMagma Glare,\nMatcho,\nMillenia-Aged Blaze,\nSmoldering Blaze,\nUnstable Magma:\n{cyclamenchance2:f}% or 1/{100/cyclamenchance2}\n\n"
        f"From:\nAshfang,\nBarbarian Duke X,\nBladesoul,\nCinderbat,\nHellwisp,\nMage Outlaw,\nMagma Boss,\nVanquisher:\n{cyclamenchance3:f}% or 1/{100/cyclamenchance3}\n")



#dark purple
darkpurplechance=(0.748*vincentmultiplier)

if dye=="dark purple":
    print("\nChance for Dark Purple Dye:\n"
        f"To appear in a Dark(er) Auction lobby: {darkpurplechance:f}% or 1/{100/darkpurplechance}\n")



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
        f"From a Beetle:        {dungchancebeetle:f}% or 1/{100/dungchancebeetle}\n"
        f"From a Cricket:       {dungchancecricket:f}% or 1/{100/dungchancecricket}\n"
        f"From an Earthworm:    {dungchanceearthworm:f}% or 1/{100/dungchanceearthworm}\n"
        f"From a Field Mouse:   {dungchancefieldmouse:f}% or 1/{100/dungchancefieldmouse}\n"
        f"From a Fly:           {dungchancefly:f}% or 1/{100/dungchancefly}\n"
        f"From a Locust:        {dungchancelocust:f}% or 1/{100/dungchancelocust}\n"
        f"From a Mite:          {dungchancemite:f}% or 1/{100/dungchancemite}\n"
        f"From a Mosquito:      {dungchancemosquito:f}% or 1/{100/dungchancemosquito}\n"
        f"From a Moth:          {dungchancemoth:f}% or 1/{100/dungchancemoth}\n"
        f"From a Rat:           {dungchancerat:f}% or 1/{100/dungchancerat}\n"
        f"From a Slug:          {dungchanceslug:f}% or 1/{100/dungchanceslug}\n")



#emerald
emeraldchance=(0.00002*bucketmultiplier*vincentmultiplier)

if dye=="emerald":
    print("\nChance for Emerald Dye:\n"
        f"Per Emerald (Ore) broken: {emeraldchance:f}% or 1/{100/emeraldchance}\n")



#flame
flamechance1=(0.00001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
flamechance2=(0.00004*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
flamechance3=(0.0001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
flamechance4=(0.0002*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)

if dye=="flame":
    print("\nChance for Flame Dye:\n"
        f"From Tier 1 Inferno Demonlord: {flamechance1:f}% or 1/{100/flamechance1}\n"
        f"From Tier 2 Inferno Demonlord: {flamechance2:f}% or 1/{100/flamechance2}\n"
        f"From Tier 3 Inferno Demonlord: {flamechance3:f}% or 1/{100/flamechance3}\n"
        f"From Tier 4 Inferno Demonlord: {flamechance4:f}% or 1/{100/flamechance4}\n")



#fossil
chiselcharges=(chiselcharges+(aquamarinemultiplier/100))
treasures=(11.5+(onyxmultiplier/100)+(fungloommultiplier/100))
highlightedtreasures=(citrinemultiplier/100)

fossilchance=(0.0002*bucketmultiplier*vincentmultiplier)
fossilchanceperscrap=(0.0002*bucketmultiplier*vincentmultiplier*treasures*((chiselcharges-highlightedtreasures)/(54-highlightedtreasures)))

if dye=="fossil":
    print("\nChance for Fossil Dye:\n"
        f"To replace any Treasure in Fossil Excavator:  {fossilchance:f}% or 1/{100/fossilchance}\n"
        f"To BE OBTAINED per scrap:                     {fossilchanceperscrap:f}% or 1/{100/fossilchanceperscrap}\n")



#frostbitten
frostbittenchance1=(0.0004*bucketmultiplier*vincentmultiplier)
frostbittenchance2=(0.001*bucketmultiplier*vincentmultiplier)
frostbittenchance3=(0.01*bucketmultiplier*vincentmultiplier)

if dye=="frostbitten":
    print("\nChance for Frostbitten Dye:\n"
        f"From Lapis Corpse:            {frostbittenchance1:f}% or 1/{100/frostbittenchance1}\n"
        f"From Umber/Tungsten Corpse:   {frostbittenchance2:f}% or 1/{100/frostbittenchance2}\n"
        f"From Vangaurd Corpse:         {frostbittenchance3:f}% or 1/{100/frostbittenchance3}\n")



#holly
hollychance=(0.00125*bucketmultiplier*vincentmultiplier)

if dye=="holly":
    print("\nChance for Holly Dye:\n"
        f"From Red Gift: {hollychance:f}% or 1/{100/hollychance}\n")



#iceberg
icerbergchance1=(0.0001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
icerbergchance2=(0.0002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
icerbergchance3=(0.002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="icerberg":
    print("\nChance for Icerberg Dye:\n\n"
        f"From:\nFrosty,\nFrozen Steve:\n{icerbergchance1:f}% or 1/{100/icerbergchance1}\n\n"
        f"From:\nNutcracker:\n{icerbergchance2:f}% or 1/{100/icerbergchance2}\n\n"
        f"From:\nYeti:{icerbergchance3:f}% or 1/{100/icerbergchance3}\n")



#jade
jadechance=(0.0002*(1+2*(rngmeteramount/5000000))*bucketmultiplier*vincentmultiplier)

if dye=="jade":
    print("\nChance for Jade Dye:\n"
        f"Per item roll in a Crystal Nucleus Bundle: {jadechance:f}% or 1/{100/jadechance}\n")



#livid
lividchance=(0.02*(1+2*(rngmeteramount/1000000))*bucketmultiplier*vincentmultiplier)

if dye=="livid":
    print("\nChance for Livid Dye:\n"
        f"From Bedrock Chest in Master Catacombs Floor V {lividchance:f}% or 1/{100/lividchance}\n")



#mango
mangochance=(0.00001*bucketmultiplier*vincentmultiplier)

if dye=="mango":
    print("\nChance for Mango Dye:\n"
          f"From breaking any log: {mangochance:f}% or 1/{100/mangochance}\n")



#matcha
matchachance1=(0.00001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
matchachance2=(0.00004*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
matchachance3=(0.0001*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
matchachance4=(0.0002*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)
matchachance5=(0.0004*(1+2*(rngmeteramount/75000000))*bucketmultiplier*vincentmultiplier)

if dye=="matcha":
    print("\nChance for Matcha Dye:\n"
        f"From Tier 1 Revenant Horror: {matchachance1:f}% or 1/{100/matchachance1}\n"
        f"From Tier 2 Revenant Horror: {matchachance2:f}% or 1/{100/matchachance2}\n"
        f"From Tier 3 Revenant Horror: {matchachance3:f}% or 1/{100/matchachance3}\n"
        f"From Tier 4 Revenant Horror: {matchachance4:f}% or 1/{100/matchachance4}\n"
        f"From Tier 5 Revenant Horror: {matchachance5:f}% or 1/{100/matchachance5}\n")



#midnight
midnightchance1=(0.0001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
midnightchance2=(0.0002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
midnightchance3=(0.002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="midnight":
    print("\nChance for Midnight Dye:\n\n"
        f"From:\nCrazy Witch,\nPhantom Spirit,\nScary Jerry,\nTrick or Treater,\nWither Gourd,\nWraith:\n{midnightchance1:f}% or 1/{100/midnightchance1}\n\n"
        f"From:\nNightmare,\nScarecrow,\nWerewolf:\n{midnightchance2:f}% or 1/{100/midnightchance2}\n\n"
        f"From:\nGrim Reaper,\nHeadless Horseman,\nPhantom Fisher:\n{midnightchance3:f}% or 1/{100/midnightchance3}\n")



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
        f"From Level 1 Potions: {mochachance1:f}% or 1/{100/mochachance1}\n"
        f"From Level 2 Potions: {mochachance2:f}% or 1/{100/mochachance2}\n"
        f"From Level 3 Potions: {mochachance3:f}% or 1/{100/mochachance3}\n"
        f"From Level 4 Potions: {mochachance4:f}% or 1/{100/mochachance4}\n"
        f"From Level 5 Potions: {mochachance5:f}% or 1/{100/mochachance5}\n"
        f"From Level 6 Potions: {mochachance6:f}% or 1/{100/mochachance6}\n"
        f"From Level 7 Potions: {mochachance7:f}% or 1/{100/mochachance7}\n"
        f"From Level 8 Potions: {mochachance8:f}% or 1/{100/mochachance8}\n")



#mythological
mythologicalchance1=(0.0001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
mythologicalchance2=(0.0002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
mythologicalchance3=(0.0004*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
mythologicalchance4=(0.002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
mythologicalchance5=(0.01*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="mythological":
    print("\nChance for Mythological Dye:\n"
        f"From:\nCretan Bull,\nMinos Hunter,\nSiamese Lynx,\nStranded Nymph:\n{mythologicalchance1:f}% or 1/{100/mythologicalchance1}\n"
        f"From:\nGaia Construct,\nHarpy:\n{mythologicalchance2:f}% or 1/{100/mythologicalchance2}\n"
        f"From:\nMinos Champion,\nMinotaur:\n{mythologicalchance3:f}% or 1/{100/mythologicalchance3}\n"
        f"From:\nMinos Inquisitor,\nSphinx:\n{mythologicalchance4:f}% or 1/{100/mythologicalchance4}\n"
        f"From:\nKing Minos,\nManticore:\n{mythologicalchance5:f}% or 1/{100/mythologicalchance5}\n")



#nadeshiko
nadeshikochance1=(0.00133*(1+2*(rngmeteramount/2500000))*bucketmultiplier*vincentmultiplier)
nadeshikochance2=(0.002*(1+2*(rngmeteramount/2500000))*bucketmultiplier*vincentmultiplier)
nadeshikochance3=(0.004*(1+2*(rngmeteramount/2500000))*bucketmultiplier*vincentmultiplier)

if dye=="nadeshiko":
    print("\nChance for Nadeshiko Dye to appear:\n"
        f"In Supreme Superpairs Experiment:         {nadeshikochance1:f}% or 1/{100/nadeshikochance1}\n"
        f"In Transcendent Superpairs Experiment:    {nadeshikochance2:f}% or 1/{100/nadeshikochance2}\n"
        f"In Metaphysical Superpairs Experiment:    {nadeshikochance3:f}% or 1/{100/nadeshikochance3}\n")



#necron
necronchance=(0.04*(1+2*(rngmeteramount/1000000))*bucketmultiplier*vincentmultiplier)

if dye=="necron":
    print("\nChance for Necron Dye:\n"
        f"From Bedrock Chest in Master Catacombs Floor VII: {necronchance:f}% or 1/{100/necronchance}\n")



#nyanza
nyanzachance=(0.0004*bucketmultiplier*vincentmultiplier)

if dye=="nyanza":
    print("\nChance for Nyanza Dye:\n"
        f"From completing a Commission: {nyanzachance:f}% or 1/{100/nyanzachance}\n")



#pearlescent
pearlescentchance1=(0.00001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
pearlescentchance2=(0.00002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
pearlescentchance3=(0.001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
pearlescentchance4=(0.002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="pearlescent":
    print("\nChance for Pearlescent Dye:\n\n"
        f"From:\nEnderman,\nEndermite,\nObsidiant Defender,\nSeer,\nZealot,\nZealot Bruiser:\n{pearlescentchance1:f}% or 1/{100/pearlescentchance1}\n\n"
        f"From:\nNest Endermite,\nVoidling Extremist,\nVoidling Fenatic:\n{pearlescentchance2:f}% or 1/{100/pearlescentchance2}\n\n"
        f"From:\nEnd Stone Protector,\nOld Dragon,\nProtector Dragon,\nSpecial Zealot,\nStrong Dragon,\nUnstable Dragon,\nWise Dragon,\nYoung Dragon:\n{pearlescentchance3:f}% or 1/{100/pearlescentchance3}\n\n"
        f"From:\nSuperior Dragon:\n{pearlescentchance4:f}% or 1/{100/pearlescentchance4}\n")



#pelt
peltchance1=(0.0004*bucketmultiplier*vincentmultiplier)
peltchance2=(0.0005*bucketmultiplier*vincentmultiplier)
peltchance3=(0.000667*bucketmultiplier*vincentmultiplier)
peltchance4=(0.001*bucketmultiplier*vincentmultiplier)
peltchance5=(0.01*bucketmultiplier*vincentmultiplier)

if dye=="pelt":
    print("\nChance for Pelt Dye:\n"
        f"From a Trackable Animal:      {peltchance1:f}% or 1/{100/peltchance1}\n"
        f"From an Untrackable Animal:   {peltchance2:f}% or 1/{100/peltchance2}\n"
        f"From an Undetected Animal:    {peltchance3:f}% or 1/{100/peltchance3}\n"
        f"From an Endangered Animal:    {peltchance4:f}% or 1/{100/peltchance4}\n"
        f"From an Elusive Animal:       {peltchance5:f}% or 1/{100/peltchance5}\n")



#periwinkle
periwinklechance1=(0.0002*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
periwinklechance2=(0.00025*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
periwinklechance3=(0.000333*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
periwinklechance4=(0.0005*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)
periwinklechance5=(0.001*bucketmultiplier*vincentmultiplier*lootingmultiplier*mfmultiplier)

if dye=="periwinkle":
    print("\nChance for Periwinkle Dye:\n"
        f"From Level 1-99 Runic Mobs:       {periwinklechance1:f}% or 1/{100/periwinklechance1}\n"
        f"From Level 100-199 Runic Mobs:    {periwinklechance2:f}% or 1/{100/periwinklechance2}\n"
        f"From Level 200-299 Runic Mobs:    {periwinklechance3:f}% or 1/{100/periwinklechance3}\n"
        f"From Level 300-399 Runic Mobs:    {periwinklechance4:f}% or 1/{100/periwinklechance4}\n"
        f"From level 400+ Runic Mobs:       {periwinklechance5:f}% or 1/{100/periwinklechance5}\n")



#sangria
sangriachance1=(0.001*(1+2*(rngmeteramount/750000))*vincentmultiplier)
sangriachance2=(0.00125*(1+2*(rngmeteramount/750000))*vincentmultiplier)
sangriachance3=(0.00167*(1+2*(rngmeteramount/750000))*vincentmultiplier)
sangriachance4=(0.0025*(1+2*(rngmeteramount/750000))*vincentmultiplier)
sangriachance5=(0.01*(1+2*(rngmeteramount/750000))*vincentmultiplier)

if dye=="sangria":
    print("\nChance for Sangria Dye:\n"
        f"From Tier 1 Riftstalker Bloodfiend: {sangriachance1:f}% or 1/{100/sangriachance1}\n"
        f"From Tier 2 Riftstalker Bloodfiend: {sangriachance2:f}% or 1/{100/sangriachance2}\n"
        f"From Toer 3 Riftstalker Bloodfiend: {sangriachance3:f}% or 1/{100/sangriachance3}\n"
        f"From Tier 4 Riftstalker Bloodfiend: {sangriachance4:f}% or 1/{100/sangriachance4}\n"
        f"From Tier 5 Riftstalker Bloodfiend: {sangriachance5:f}% or 1/{100/sangriachance5}\n")



#secret
secretchance=(0.0001*bucketmultiplier*vincentmultiplier)

if dye=="secret":
    print("\nChance for Secret Dye:\n"
        f"From Collecting a Secret: {secretchance:f}% or 1/{100/secretchance}\n")



#tentacle
tentaclechance1=(0.001*bucketmultiplier*vincentmultiplier)
tentaclechance2=(0.00125*bucketmultiplier*vincentmultiplier)
tentaclechance3=(0.00167*bucketmultiplier*vincentmultiplier)
tentaclechance4=(0.0025*bucketmultiplier*vincentmultiplier)
tentaclechance5=(0.005*bucketmultiplier*vincentmultiplier)

if dye=="tentacle":
    print("\nChance for Tentacle Dye:\n"
        f"From a Basic Tier Kuudra Loot Chest:      {tentaclechance1:f}% or 1/{100/tentaclechance1}\n"
        f"From a Hot Tier Kuudra Loot Chest:        {tentaclechance2:f}% or 1/{100/tentaclechance2}\n"
        f"From a Burning Tier Kuudra Loot Chest:    {tentaclechance3:f}% or 1/{100/tentaclechance3}\n"
        f"From a Fiery Tier Kuudra Loot Chest:      {tentaclechance4:f}% or 1/{100/tentaclechance4}\n"
        f"From an Infernal Tier Kuudra Loot Chest:  {tentaclechance5:f}% or 1/{100/tentaclechance5}\n")



#treasure
treasurechance1=(0.0001*bucketmultiplier*vincentmultiplier)
treasurechance2=(0.001*bucketmultiplier*vincentmultiplier)
treasurechance3=(0.01*bucketmultiplier*vincentmultiplier)

if dye=="treasure":
    print("\nChance for Treasure Dye:\n"
        f"From a Good Catch:            {treasurechance1:f}% or 1/{100/treasurechance1}\n"
        f"From a Great Catch:           {treasurechance2:f}% or 1/{100/treasurechance2}\n"
        f"From an Outstanding Catch:    {treasurechance3:f}% or 1/{100/treasurechance3}\n")



#wild strawberry
wildstrawberrychance=(0.000000667*bucketmultiplier*vincentmultiplier)

if dye=="wild strawberry":
    print("\nChance for Wild Strawberry Dye:\n"
        f"From Harvesting a Crop: {wildstrawberrychance:f}% or 1/{100/wildstrawberrychance}\n")



#close program
input('Press Enter to exit. ')