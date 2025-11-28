#input bucket of dye

#imports
from functions import input_dye
from lists import all_dyes_bucketofdye_list

dye=input_dye.getdye()

#input bucket of dye
global bucketofdye
bucketofdye=False

def input_bucket_of_dye():
    bucketmultiplier=1
    if dye in all_dyes_bucketofdye_list.bucketofdyeList:
        while True:
            global bucketofdye
            bucketofdye=input("Do you have a Bucket Of Dye? (Yes/No): ")
            bucketofdye=bucketofdye.lower()
            if bucketofdye=="yes":
                bucketmultiplier=1.01
                break
            elif bucketofdye=="no":
                break
            else:
                print("Invalid input! Please say 'Yes' or 'No'!")
    return bucketmultiplier

def getbucketofdye():
    return bucketofdye