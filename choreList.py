

from datetime import datetime


TODO = ["Vacuum", "Sweep", "Laundry"]

print("CHORES LIST!\nThere are", len(TODO),"things on the list")
print("they are:\n")
for i in TODO:
    print(i)

TODO.append("Dusting")

print("I have updated the list, there are now", len(TODO), "on the list\n")
for i in TODO:
    print(i)


choreList ={
    1:"Vacuum",
    2:"Sweep",
    3:"Laundry",
    4:"Dusting"
}
running = True

while running:
    guesse = int(input("#Guess between numbers 1 - 4 to find out what your chore is\nEnter number here:"))
    running

    if guesse not in choreList:
        print("Invalid number, please try again.")
    else:
        print(f"Your chore is {choreList[guesse]}")


print("\n*This chore was created at* \n", datetime.now())

