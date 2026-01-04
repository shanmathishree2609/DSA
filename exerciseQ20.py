shopping_list = []
while True:
    action = input("What do you want to do? (add/remove/show/quit): ").lower() 
    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "added.")  
    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed.")
        else:
            print(item, "not found in the list.")       
    elif action == "show":
        print("Shopping list:", shopping_list) 
    elif action == "quit":
        print("Goodbye!")
        break
    else:
        print("Please type add, remove, show, or quit.")
