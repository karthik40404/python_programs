from reg import register
from tab import table

data = []

while True:
    print("1. Add \n2. View \n3. Update \n4. Delete \n5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        register(data)
    elif ch == 2:
        table(data)
    # elif ch == 3:
    #     id_to_update = int(input("Enter the ID to update: "))
    #     for record in data:
    #         if record['id'] == id_to_update:
    #             record['name'] = input("Enter new Name: ")
    #             record['age'] = int(input("Enter new Age: "))
    #             record['place'] = input("Enter new Place: ")
    #             print("Record updated")
    #             break
    #     else:
    #         print("ID not found")
    # elif ch == 4:
    #     id_to_delete = int(input("Enter the ID to delete: "))
    #     for record in data:
    #         if record['id'] == id_to_delete:
    #             data.remove(record)
    #             print("Record deleted")
    #             break
    #     else:
    #         print("ID not found")
    # elif ch == 5:
    #     print("Exiting the program.")
    #     break
    # else:
    #     print("Invalid choice, please try again.")
