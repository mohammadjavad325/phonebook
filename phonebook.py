# دفترچه تلفن ساده - فقط با اجرای پایتون باز میشه

contacts = [
    {"name": "Ali", "phone": "09121234567"},
    {"name": "Sara", "phone": "09351234567"},
    {"name": "Reza", "phone": "09012345678"},
    {"name": "Niloofar", "phone": "09221234567"},
    {"name": "Mohammad", "phone": "09901234567"}
]

def show_menu():
    print("\n📱 Phone Book Menu:")
    print("1. Show all contacts")
    print("2. Add new contact")
    print("3. Search by name")
    print("4. Delete contact")
    print("5. Exit")

def show_contacts():
    if not contacts:
        print("📭 Contact list is empty.")
    else:
        print("\n📝 All Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. 👤 {contact['name']} - 📞 {contact['phone']}")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    print("✅ Contact added successfully!")

def search_contact():
    search = input("Enter name to search: ").lower()
    found = False
    for contact in contacts:
        if contact["name"].lower() == search:
            print(f"🔍 Found: {contact['name']} - {contact['phone']}")
            found = True
    if not found:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("🗑️ Contact deleted.")
            return
    print("❌ Contact not found.")

# اجرای منو
while True:
    show_menu()
    choice = input("Select an option (1-5): ")

    if choice == "1":
        show_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid option, please choose from 1 to 5.")
