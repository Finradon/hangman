import re
import random

exec(open("hangmanwordbank.py").read())

#word = input("Input the word: ")
word = words[random.randint(0,len(words))]

i = 0
solved = False

length = len(word)
line = length * "_ "
print(line)
linelist = list(line)

while solved == False:
    letter = input("Type a letter: ")
    

    if len(letter) > 1:
        print("Please type a single letter.")
    else: 
        if letter in word:
            print("The letter "+ letter + " is in the word!")
            pos = [m.start() for m in re.finditer(letter, word)]
            
            for index in pos:
                linelist[2*index] = letter

            line = "".join(linelist)
            print(line)
            
            if line.find("_") == -1:
                print("You won! The word was " + word)
                solved = True
        else:
            print("The letter "+ letter + " is not in the word.")
            print(HANGMANPICS[i])
            i += 1
            
            if i == 7:
                print("You lost :(.")
                quit()

