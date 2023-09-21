import functionTodo
import PySimpleGUI as sg
import time

clock = sg.Text('', key= 'clock')
lable = sg.Text('Type in a todo list')
input_box = sg.InputText(tooltip='Enter todo here', key = 'todo')
add_button = sg.Button('Add')

todo_list = sg.Listbox(values= functionTodo.get_todo(), key = 'todos',
                        enable_events=True, size=[50,20])
edit_button = sg.Button('Edit')

complete_button = sg.Button('Complete')
Exit_button = sg.Button('Exit')

window = sg.Window('My to do App', layout=[[clock],[lable],
                                            [input_box, add_button],
                                            [todo_list, edit_button, complete_button],
                                            [Exit_button]])

while True:
    event, value = window.read(timeout=200)
    print(event)
    print(value)
    #print(value['todos'][0])
    #y this error : TypeError: 'NoneType' object is not subscriptable ?? 
    window['clock'].update(value=time.strftime('%b-%d-%Y %H:%M'))
    match event:
        case 'Add':
            try:
                todos = functionTodo.get_todo()
                new_todo = value['todo'] + "\n" 
                todos.append(new_todo)
                functionTodo.write_todos(todos)
                window['todos'].update(values= todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup(' Please write a todo 1st')
        case 'Edit':
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo'] +'\n'
                todos = functionTodo.get_todo()
                index = todos.index(todo_to_edit)
                todos[index]= new_todo
                functionTodo.write_todos(todos)

                window['todos'].update(values= todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup(' Please select a todo 1st')
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case 'Complete':
            try:
                todo_complete = value['todos'][0]
                todos = functionTodo.get_todo()
                todos.remove(todo_complete)
                functionTodo.write_todos(todos)
                window['todos'].update(values= todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup(' Please select a todo 1st')
        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break


window.close()