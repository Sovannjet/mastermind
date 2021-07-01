import random

# make code & start game
colors = ["r", "o", "y", "g", "b", "v"]
code = ""
for x in range(4):
    rd = random.choice(colors)
    code += rd
    colors.remove(rd)
print("The code has been made!")
print("The color options are r, o, y, g, b, v.")
print("'r' represents a red peg, 'w' represents a white peg, and '-' represents an empty hole.")

# run through 10 guesses/trials
k = 1
correct = False
while k <= 10 and correct is False:
    guess = input("Input guess # " + str(k) + ": ")
    grade = ""
    colorsAlreadyChecked = set()
    count = 0  # keeps track of how many pegs have been placed

    # grade the guess and output appropriate pegs
    if guess == code:
        correct = True
        print("Correct!")
    else:
        for h in range(4):  # check for correct color & location (red peg)
            if guess[h] == code[h]:
                grade += "r"
                count += 1
                colorsAlreadyChecked.add(guess[h])
        for i in range(4):  # check for correct color (white peg)
            if guess[i] not in colorsAlreadyChecked:
                for j in range(4):
                    if guess[i] == code[j]:
                        grade += "w"
                        count += 1
            colorsAlreadyChecked.add(guess[i])
        for x in range(4-count):
            grade += "-"
        print(grade)

    k += 1

print("The code was: " + code)
print("Thanks for playing!")