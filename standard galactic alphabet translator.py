#standard galactic alphabet translator 

#to do:
    #

#Standard Galactic Alphabet dictionary
sgaDict={
    "A":"ᔑ ",
    "B":"ʖ ",
    "C":"ᓵ ",
    "D":"↸ ",
    "E":"ᒷ ",
    "F":"⎓ ",
    "G":"⊣ ",
    "H":"⍑ ",
    "I":"╎ ",
    "J":"⋮ ",
    "K":"ꖌ ",
    "L":"ꖎ ",
    "M":"ᒲ ",
    "N":"リ ",
    "O":"𝙹 ",
    "P":"!¡ ",
    "Q":"ᑑ ",
    "R":"∷ ",
    "S":"ᓭ ",
    "T":"ℸ. ",
    "U":"⚍ ",
    "V":"⍊ ",
    "W":"∴ ",
    "X":"̇/ ",
    "Y":"|| ",
    "Z":"⨅ "}

#translator
userinput=input("What would you like to be translated?: ")
translation=""
for char in userinput.upper():
    if char in sgaDict:
        translation+=sgaDict[char]
    elif char=="\\":
        translation+="\n"
    else:
        translation+=char
print(f"Translation: {translation}")