# import gui library
import PySimpleGUI as pysg

# set gui color scheme
pysg.theme("darkbrown7")

# set gui layout
layout = [[pysg.Text("Select Operation: "), 
           pysg.Radio("Create", "operation", key="create",enable_events=True), 
           pysg.Radio("Read", "operation", key="read", enable_events=True), 
           pysg.Radio("Update", "operation", key="update", enable_events=True), 
           pysg.Radio("Delete", "operation", key="delete", enable_events=True)],
          [pysg.Text("Enter Title:", key="title_text"), 
           pysg.Input(key="title", expand_x=True)],
          [pysg.Text("Output:", key="output_text"), 
           pysg.Multiline(key="list", expand_x=True, expand_y=True, pad=14)],
          [pysg.Button("Execute", key="execute"), pysg.Button("Exit")]]

# create window object
window = pysg.Window("SQL Movie Library Catalog", layout, resizable=True, finalize=True)

# hide elements until user selects operation
window["title_text"].update(visible=False)
window["title"].update(visible=False)
window["output_text"].update(visible=False)
window["list"].update(visible=False)
window["execute"].update(visible=False)

# set event loop
while True: 

    # read window for events and collect values
    event, values = window.read()

    # if user clicks exit or the exit button in top right of window, end loop
    if event in (None, "Exit"):
        break
    
    if event in "create":
        print("Perform create function.")

    elif event in "read":
        print("Perform read function")

    elif event in "update":
        print("Perform update function")

    elif event in "delete":
        print("Perform delete function")
    
    
    
    # if user enters data in the input field, copy that into the output field
    # if event in ("Execute"):
    #     window["list"].update(values["name_in"])

# close window and end program
window.close()
