import streamlit as st
import functionTodo

st.title(' Fun ToDo App')
st.subheader('This is my Todo app')
st.write('It will help you increase your productivity')

todos = functionTodo.get_todo()

def add_todo():
        todo = st.session_state['new_todo']
        todos.append(todo + '\n')
        functionTodo.write_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
          todos.pop(index)
          functionTodo.write_todos(todos)
          del st.session_state[todo]
          st.experimental_rerun()
          


st.text_input(label= 'Enter todo here :', 
              placeholder= 'write todo to be added to the list',
              on_change=add_todo, key='new_todo')
