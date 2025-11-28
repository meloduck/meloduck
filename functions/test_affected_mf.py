#test if dye is affected by mf

#imports
from functions import input_dye
from lists import all_dyes_mf_list

dye=input_dye.getdye()

#is the dye affected by magic find (and looting)?
def testmfaffected():
    magicfindaffected=False
    if dye in all_dyes_mf_list.mfList:
        magicfindaffected=True
    return magicfindaffected