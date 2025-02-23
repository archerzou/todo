import FreeSimpleGUI as sG
import functions

label = sG.Text("Type in a to-do")
input_box = sG.InputText(tooltip="Enter a to-do", key="todo")
add_button = sG.Button("Add")

window = sG.Window("My To-Do App",
                   layout=[[label],[input_box, add_button]],
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
        case sG.WINDOW_CLOSED:
            break

window.close()