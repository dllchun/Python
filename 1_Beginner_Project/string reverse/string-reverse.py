def get_string():
     oldString = input('Please input your string? ')
     return oldString
     

def string_reverse():
    while True:
        world_list = []
        oldString = get_string()
        if oldString == 'Stop':
            break
        else: 
            for i in oldString:
                world_list.insert(0, i)
                
            print(''.join(world_list))
        
        
string_reverse()