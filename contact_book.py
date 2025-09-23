from datetime import datetime

print("Black Book")

#Contact dictionary
contacts = {
    "Brandon":"Backend Dev",
    "Andrew": "Frontend Dev",
    "Anthony": "Data Analyst"
}

#Function to show contacts
def show_contacts():
    print("There are 4 contacts in my blackbook, their names are")
    for name, role in contacts.items():
        print(f"{name}: {role}")

#Function to add contacts
def addContacts(name, role):
    print("I added another contact, here is the new list")
    contacts[name] = role
    for name, role in contacts.items():
        print(f"{name}: {role}")

if __name__ == "__main__":
    show_contacts()
    addContacts("Shaun", "Cloud Engineer")
    print("This was printed on", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))