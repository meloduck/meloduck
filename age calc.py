#age calculator

birthyear=input("In what year were you born?: ")

import datetime

hasaged=input("Have you already celebrated your birthday this year?: ")
if hasaged.strip().lower()=="nee":
    birthyear=datetime.datetime.now().year-int(birthyear)-1
else:
    birthyear=datetime.datetime.now().year-int(birthyear)
print("You are",birthyear,"Years old.")