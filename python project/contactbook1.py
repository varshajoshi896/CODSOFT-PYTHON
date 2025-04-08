contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    query = input("Enter name of contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == query:
            print("Leave field blank to keep current value.")
            new_name = input(f"New name ({contact['name']}): ") or contact['name']
            new_phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"New email ({contact['email']}): ") or contact['email']
            new_address = input(f"New address ({contact['address']}): ") or contact['address']
            contact.update({"name": new_name, "phone": new_phone, "email": new_email, "address": new_address})
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    query = input("Enter name of contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == query:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\n====== Contact Book Menu ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Contact Book
main()
