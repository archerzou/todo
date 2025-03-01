import FreeSimpleGUI as sG
import functions

label = sG.Text("Type in a to-do")
input_box = sG.InputText(tooltip="Enter a to-do", key="todo")
add_button = sG.Button("Add")
list_box = sG.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])

edit_button = sG.Button("Edit")

window = sG.Window("My To-Do App",
                   layout=[[label],[input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            print(todos)
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sG.WINDOW_CLOSED:
            break

window.close()