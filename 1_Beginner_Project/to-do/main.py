todos = []

while True:
    user_action = input("Type add, show, edit, complete or exittt:  ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1} -- {item}")
        case "edit":
            item_to_be_edit = input('what would you like to change: ')
            position = todos.index(item_to_be_edit)
            new_item = input("what would you like to change to: ")
            todos[position] = new_item
            
        case "complete":
            item_completed = input('which item did you completed? ')
            position = todos.index(item_completed)
            todos.pop(position)
            
            
            
        case 'exit':
            break

        case _:
            print('you have answered an unknown command')
print('bye')


#test
