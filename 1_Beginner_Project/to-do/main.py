while True:
    user_action = input("Type add, show, edit, complete or exit:  ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("1_Beginner_Project/to-do/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("1_Beginner_Project/to-do/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("1_Beginner_Project/to-do/todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                print(f"{index + 1} -- {item}")
        case "edit":
            item_to_be_edit = input("what would you like to change: ")
            position = todos.index(item_to_be_edit)
            new_item = input("what would you like to change to: ")
            todos[position] = new_item

        case "complete":
            item_completed = input("which item did you completed? ")
            position = todos.index(item_completed)
            todos.pop(position)

        case "exit":
            break

        case _:
            print("you have answered an unknown command")
print("bye")
