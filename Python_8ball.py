import sys
import random

print("What is your name?")
name = input()
print('Hello ' + name)
#This will prompt the user to input their name and then print their name.

A = ["Of course!", "Without a doubt!", "Unfortunately not", "That is always a possibility",
     "No", "If it's in the cards for you!", "I can see that in your future"]
Q = True
#These are the answers that the program will respond with after each question.

while Q:
    quest = input("Please ask me any question (press enter to exit program)")

    if quest == "":
        sys.exit()

    else:
        print(A[random.randint(0,6)])
#This randmomizes answers to each question.

    quest = input("Please ask another question")
