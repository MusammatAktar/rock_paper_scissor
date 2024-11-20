# welcoming player and giving instructions 
print("Welcome Boddies!")
print("when asked for your choice please enter r, p, or s")

# geting players inout
playerOneInput = input("player one select: r, p, or s;")
playerTwoInput = input("player two select: r, p, or s;")
print("player one input:" + playerOneInput + "\n" + "player two input: " + playerTwoInput)

# compare player input to determine result. Either player one wins, player two winds, or it's a tie 
# scissors
if playerOneInput == "s":
    if playerTwoInput == "s":
        print("Tied!!")
    if playerTwoInput == "r":
        print("player two wins!!!")
    if playerTwoInput == "p":
        print("player one wins!!!")

# paper
if playerOneInput == "p":
    if playerTwoInput == "p":
        print("Tied!!")
    if playerTwoInput == "r":
        print("player one wins!!!")
    if playerTwoInput == "s":
        print("player two wins!!!")

# rock
if playerOneInput == "r":
    if playerTwoInput == "r":
        print("Tied!!")
    if playerTwoInput == "s":
        print("player one wins!!!")
    if playerTwoInput == "p":
        print("player two wins!!!")