
TODO = ["Vacuum", "Sweep", "Laundry"]


print("CHORE LIST!!")

def toDoList(TODO):
    print("The current todo list,\nhas", len(TODO), "items left on it, here they are\n")
    for i in TODO:
        print(i)

def addItem(TODO):
    TODO.append("Dusting")
    print("\nI have added another item. Here is the new list\n")
    for i in TODO:
        print(i)

choreList = {
        1:"Vacuum",
        2:"Sweep",
        3:"Laundry",
        4:"Dusting"
    }

def guess():   
    while True:
        guess = int(input("\nChoose between numbers 1 - 4 to determine your chore.\nEnter number here:"))
        if guess not in choreList:
            print("Invalid number, please try again")
        else:
            print(f"Your chore will be", choreList[guess])

if __name__=="__main__":
    toDoList(TODO)
    addItem(TODO)
    choreList
    guess()