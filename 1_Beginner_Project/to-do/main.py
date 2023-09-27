todos = []

while True:
    user_action = input("Type add, show, edit or exit:  ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            item_to_be_edit = input('what would you like to change: ')
            position = todos.index(item_to_be_edit)
            new_item = input("what would you like to change to: ")
            todos[position] = new_item
        case 'exit':
            break

        case _:
            print('you have answered an unknown command')
print('bye')