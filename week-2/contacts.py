contact_book = {}

def add_contact():
    global contact_book
    key = input("Enter a name: ")
    value = int(input("Enter a phone number: "))
    contact_book[key] = value
    print("Contact added successfully!")

def search_contact():
   key2 = input("Enter the name to search: ")
   if key2 in contact_book:
       print("Phone number for " + key2 + ": " + str(contact_book[key2]))
   else:
       print("Contact not found")

def update_contact():
    global contact_book
    key = input("Enter the name to update: ")
    if key in contact_book:
        value2 = input("Enter the new phone number: ")
        contact_book[key] = value2
        print("Contact updated")
    else:
        print("Contact not found")

def delete_contact():
    global contact_book
    key = input("Enter the name to delete: ")
    if key in contact_book:
        del contact_book[key]
        print("Contact deleted")
    else:
        print("Contact not found")

# To check the above functions are working properly or not
def view_contacts():
    if not contact_book:
        print("Your contact book is empty")
    else:
        print("--- All Contacts ---")
        for key,value in contact_book.items():
            print("Name: " + key +  "   Phone number: " + str(value))
        
while True:
    print("--- Contact Book ---")
    print("1. Add a contact")
    print("2. Search a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. View all contacts")

    choice = int(input("Choose an option (1 - 5): "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        update_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        view_contacts()
    else:
        print("Invalid choice! Please select between 1 and 5")                
    
    
