#test if dye is affected by ff

#imports
from functions import input_dye
from lists import all_dyes_ff_list

dye=input_dye.getdye()

#is the dye affected by farming fortune?
def testffaffected():
    farmingfortuneaffected=False
    if dye in all_dyes_ff_list.ffList:
        farmingfortuneaffected=True
    return farmingfortuneaffected