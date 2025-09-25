# contact book 
contact={}
def add_contact():
    name=input(" enter name")
    phone_no = input(" enter phone no.").strip()
    email=input(" enter eamil").strip()
    address=input(" enter address")
    if name == "" and phone_no == "":
        print("Error:name and phone number is required")
        return
    else:
        contact[name]={"phone":phone_no,"email":email,"address":address}
        print("contact added successfully!\n")
def view_contacts():
    if not contact:
        print("no contact found!\n")
        return
    for name,details in contact.items():
        print(f"name:{name}")
        print(f"phone:{details['phone']}")
        print(f"eamil:{details['email']}")
        print(f"adress:{details['address']}\n")
def search_contact():
    search=input("enter name or phone to search: ").strip().lower()
    found=False
    for name,details in contact.items():
        if search in name.lower() or search in details['phone']:
            print(f"\n contact found:")
            print(f"name:{name}")
            print(f"phone:{details['phone']}")
            print(f"eamil:{details['email']}")
            print(f"adress:{details['address']}\n")
            found=True
    if not found:
        print("no matching contact found.\n")
def update_contact():
    name=input("enter name of the contact to update:").strip()
    if name not in contact:
        print(f"not found! with name '{name}'\n")
        return
    print("enter new details (leave blank to keep the current value):\n")
    phone=input(f"phone[{contact[name]['phone']}]: ").strip()
    email=input(f"email[{contact[name]['email']}]:").strip()
    address=input(f"address[{contact[name]['address']}]: ").strip()
    if phone:
        contact[name]['phone']=phone
    if email:
        contact[name]['email']=email
    if address:
        contact[name]['address']=address
    print(f"contact '{name}' updated successfully!\n")
def delete_contact():
    name=input(" enter name of the contact to delete: ").strip()
    if name not in contact:
        print("no contact found with name '{name}'\n")
        return
    confirm=input(f"are you sure you want to delete '{name}'? (Y/N)").strip().lower()
    if confirm=="y":
        del contact[name]
        print(f"contact '{name}' deleted successfully!\n")
    else:
        print("deletation cancelled.\n")
def book():
    while True:
        print("1.Add contact")
        print("2.delete contact")
        print("3.update contact")
        print("4.view all contact")
        print("5.search contact")
        print("6.exit\n")
        choice =input(" enter choice\n")
        if choice=="1":
            add_contact()
        elif choice=="2":
            delete_contact()
        elif choice=="3":
            update_contact()
        elif choice=="4":
            view_contacts()
        elif choice=="5":
            search_contact()
        elif choice=="6":
            print("Exiting contact book !\n")
            break
        else:
            print("Invalid Choice! Please enter valid choice\n")
if __name__=="__main__":
    book()
    

