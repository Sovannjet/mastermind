import random

# make code & start game
colors = ["r", "o", "y", "g", "b", "v"]
code = ""
for x in range(4):
    rd = random.choice(colors)
    code += rd
    colors.remove(rd)
colors = ["r", "o", "y", "g", "b", "v"]  # reset colors
print("The code has been made!")
print("The color options are r, o, y, g, b, v.")
print("'r' represents a red peg, 'w' represents a white peg, and '-' represents an empty hole.")

# run through 10 guesses/trials
k = 1
correct = False
while k <= 10 and correct is False:
    guess = input("Input guess #" + str(k) + ": ").lower()

    # remove spaces
    guessWithSpacesRmvd = ""
    for i in range(len(guess)):
        if guess[i] != " ":
            guessWithSpacesRmvd += guess[i]
    guess = guessWithSpacesRmvd

    # check string for non-roygbv chars
    hasNonRoygbvChars = False
    i = 0
    while i < len(guess) and hasNonRoygbvChars is False:
        if guess[i] not in colors:
            hasNonRoygbvChars = True
        i += 1

    # check string for length and non-roygbv colors, before grading
    if len(guess) != 4:
        print("Your guess should be four items long.")
    elif hasNonRoygbvChars:
        print("Your guess should only consist of the letters r, o, y, g, b, and v.")
    else:  # grade the guess and output appropriate pegs
        grade = ""
        colorsAlreadyChecked = set()
        numPegsPlaced = 0

        if guess == code:
            correct = True
            print("Correct!")
        else:
            for h in range(4):  # check for correct color & location (red peg)
                if guess[h] == code[h]:
                    grade += "r"
                    numPegsPlaced += 1
                    colorsAlreadyChecked.add(guess[h])
            for i in range(4):  # check for correct color (white peg)
                if guess[i] not in colorsAlreadyChecked:
                    for j in range(4):
                        if guess[i] == code[j]:
                            grade += "w"
                            numPegsPlaced += 1
                colorsAlreadyChecked.add(guess[i])
            grade += "-" * (4-numPegsPlaced)
            print(grade)

        k += 1

print("The code was: " + code)
print("Thanks for playing!")
