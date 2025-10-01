#leeftijd uitrekenen

geboortejaar=input("In welk jaar ben je geboren?: ")

import datetime

aljarig=input("Ben je dit jaar al jarig geweest?: ")
if aljarig.strip().lower()=="nee":
    leeftijd=datetime.datetime.now().year-int(geboortejaar)-1
else:
    leeftijd=datetime.datetime.now().year-int(geboortejaar)
print("Je bent",leeftijd,"jaar oud.")