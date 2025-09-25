inventory = {
    1: {"Beer" : 30},
    2: {"Wine": 100}, 
    3: {"Cognac" : 33},
    4: {"Seltzers" : 25}
}

def cases():
    while True:

        dept = (input("Enter department number, (or 'q' to quit):"))
        if dept.lower() == 'q':
            print("Exiting..")
            break

        if not dept.isdigit() or int(dept) not in inventory:
            print("Invalid department")
        else:
            dept = int(dept)
            dept_data = inventory[dept]
            for name, count in dept_data.items():
                print(f"{name}: {count}")

if __name__ == "__main__":
    cases()
