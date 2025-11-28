#input crop fortune and test for int, if not int return "Invalid input!" and try again

#imports

#testintcf
def testintcf(prompt):
    testintcfinput=0

    while True:
        testintcfinput=input(f"How much {prompt} Fortune do you have? (With Vacuum equipped!): ")
        try:
            testintcfinput=int(testintcfinput)
            if testintcfinput>=0:
                break
            elif testintcfinput<0:
                print(f"You can't have negative {prompt} Fortune!")
        except:
            print("Invalid input!")
    return testintcfinput