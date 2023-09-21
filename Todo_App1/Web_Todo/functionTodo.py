FILEPATH = 'todolist.txt'

def get_todo(file_path = 'todolist.txt'):
    # read the text file and return todo list 
    with open(file_path, 'r') as file:
        todo= file.readlines()
    return todo

def write_todos(todo_args, filePath = 'todolist.txt'):
    #write the tet iteams in the todo list file 
    with open(filePath,'w') as file:
            file.writelines(todo_args)

if __name__ == '__main__':
    print('Hello')
    print(get_todo())


