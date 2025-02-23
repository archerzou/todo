import FreeSimpleGUI as sG

label = sG.Text("What are dolphins?")
option1 = sG.Radio("Amphibians", group_id="question1")
option2 = sG.Radio("Fish", group_id="question1")
option3 = sG.Radio("Mammals", group_id="question1")
option4 = sG.Radio("Birds", group_id="question1")

window = sG.Window("File Compressor",
                   layout=[[label],
                           [option1],
                            [option2],
                            [option3],
                            [option4],
                           ])

window.read()
window.close()