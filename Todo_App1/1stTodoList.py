#User_prompt = 'Enter your Todos...'

#todolist=[]
from functionTodo import get_todo, write_todos
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is '+ now)

while True:
    todo = input('Type add ,show, edit, complete or exit :  ')
    todo = todo.strip()

    if todo.startswith('add'):
        todo_add = todo[4:]
        todolist = get_todo()
        todolist.append(todo_add +'\n')
        print(todo_add,' : Todo had been succefully Added')
        write_todos( todolist)
        
    elif todo.startswith('show'):
        with open('todolist.txt', 'r') as file: 
            todolist = file.readlines()
        #print(*enumerate.todolist)
        
        for  i,task in enumerate(todolist,1):
            print('{}-{}'.format(i, task.title().strip('\n')))
    elif todo.startswith('edit'):
        try:
            number = int(todo[5:])
            #number = int(number)
            todolist = get_todo()
            todolist[number-1] = input('enter new todo here : ')+'\n'
            write_todos(todolist)
            print((todolist[number-1]).strip('\n'),' : Todo had been succefully updated')
        except ValueError:
            print('invalid command')
            continue
    elif todo.startswith('complete'):
        try:
            number = int(todo[8:])
            print(number)
            todolist = get_todo()
            print((todolist[number-1]).strip('\n'), ' is removed from the list')
            todolist.pop(number-1)
            write_todos(todolist)
        except ValueError:
            print('Invalid command : try puting in the # number of todo')
            continue
        
    elif todo.startswith('exit'):
        print('ok byee')
        break
    else:
        print('unknown command')
        #continue

    #print(todolist)