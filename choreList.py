

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


number = 1,2,3,4
running = True

while running:
    guesse = int(input("#Guess between numbers 1 - 4\nEnter number here:"))
    running
    if guesse > 4:
        print("That is not a valid number, please try again.")
    if guesse < 1:
        print("That is not a valid number, please try again.")
    if guesse == 1:
        print("You chore is Vacuuming")
        break
    if guesse == 2:
        print("Your chore is Laundry")
        break
    if guesse == 3:
        print("Your chore is Dusting")
        break
    if guesse == 4:
        print("Your chore is Sweeping")

print("\n*This chore was created at* \n", datetime.now())

