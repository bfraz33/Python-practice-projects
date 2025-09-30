import json
import os

# Load existing inventory if it exists, otherwise use default
if os.path.exists("current_inventory.json"):
    with open("current_inventory.json", "r") as f:
        inventory = json.load(f)
    # Convert keys back to int since JSON saves them as strings
    inventory = {int(k): v for k, v in inventory.items()}
else:
    inventory = {
        1: {"Beer": 30},
        2: {"Wine": 100},
        3: {"Cognac": 33},
        4: {"Seltzers": 25}
    }

def cases():
    while True:
        dept = input("Enter department number (ENTER to quit): ")

        if dept == "":  # quit loop
            print("Exiting...")
            break

        if not dept.isdigit() or int(dept) not in inventory:
            print("Invalid department")
            continue

        dept = int(dept)
        dept_data = inventory[dept]
        for name, count in dept_data.items():
            print(f"{dept}. {name}: {count} cases")

        qty(dept)

def qty(dept):
    dept_data = inventory[dept]

    sold_input = input("How many were sold? (negative for returns, ENTER to quit): ")

    if sold_input == "":
        return 

    try:
        sold = int(sold_input)
    except ValueError:
        print("Invalid number. Try again.")
        return

    for name, count in dept_data.items():
        dept_data[name] = count - sold
        print(f"{dept}. {name}: {dept_data[name]} cases")

    # Save updated inventory
    with open("current_inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

if __name__ == "__main__":
    cases()
