#test if dye is affected by RNG meter

#imports
from functions import input_dye
from lists import all_dyes_rngmeter_list

dye=input_dye.getdye()

#is the dye affected by RNG meter?
def testrngaffected():
    rngaffected=False
    if dye in all_dyes_rngmeter_list.rngList:
        rngaffected=True
    return rngaffected