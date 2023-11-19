# import gui library
import PySimpleGUI as pysg

# import sql library
import sqlite3

# import csv library
import csv

# read movie csv file into list
# create an empty list.
movie_list = []

# prepare for error
try:

    # open the CSV file for reading.
    with open("../movies.csv", "rt") as csv_file:

        # use the csv library to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # Process each row in the CSV file.
        for i, row in enumerate(reader):

            # add id (primary key) to list
            row.insert(0, i + 1)

            # change bookcase and shelf to int
            row[2] = int(row[2])
            row[3] = int(row[3])

            # change stack to int
            if row[4] != "":
                row[4] = int(row[4])
            else:
                row[4] = 0

            # add row to list
            movie_list.append(row)

# handle any errors
except Exception as e:
    print(f"Error reading movies.csv\n{e}\n")

# create the connection to the database
connection = sqlite3.connect("movies.db")

# create the tables in movies.db
cur = connection.cursor()

# if movies.db tables do not exist, create them
cur.execute('''
            CREATE TABLE IF NOT EXISTS movies 
            (id int PRIMARY KEY, title text, bookcase int, shelf int, stack int)
            ''')

# loop through movies list and format according to db layout
for i, movie_row in enumerate(movie_list):
    
    # if stack is None, set as zero, otherwise change text to int
    if movie_row[3] != '':
        movie_list[i][3] = int(movie_row[3])
    else:
        movie_list[i][3] = 0

# if movies are not in the db, insert them
cur.executemany("INSERT OR IGNORE INTO movies VALUES (?, ?, ?, ?, ?)", movie_list)
connection.commit()

# set gui color scheme
pysg.theme("darkbrown7")

def hide_elements(window):
    window["title_text"].update(visible=False)
    window["title"].update(visible=False)
    window["output_text"].update(visible=False)
    window["list"].update(visible=False)
    window["execute"].update(visible=False)
    window["delete_title"].update(visible=False)
    window["title_delete"].update(visible=False)
    window["deleted"].update(visible=False)

def show_read_elements(window):
    window["title_text"].update(visible=True)
    window["title"].update(visible=True)
    window["output_text"].update(visible=True)
    window["list"].update(visible=True)
    window["execute"].update(visible=True)

def show_delete_elements(window):
    
    window["delete_title"].update(visible=True)
    window["title_delete"].update(visible=True)
    window["deleted"].update(visible=True)


# set gui layout
layout = [
          [pysg.Text("Select Operation: "), 
           pysg.Radio("Create", "operation", key="create",enable_events=True), 
           pysg.Radio("Read", "operation", key="read", enable_events=True, default=True), 
           pysg.Radio("Update", "operation", key="update", enable_events=True), 
           pysg.Radio("Delete", "operation", key="delete", enable_events=True)],
          [pysg.Text("Enter Title:", key="title_text"), 
           pysg.Input(key="title", expand_x=True)],
          [pysg.Text("Output:", key="output_text"), 
           pysg.Multiline(key="list", expand_x=True, expand_y=True, pad=14)],
          [pysg.Text("Delete Title: ", key="delete_title"),
           pysg.Input(key="title_delete", expand_x=True)],
          [pysg.Text("", key="deleted")],
          
          [pysg.Button("Execute", key="execute"), pysg.Button("Exit")],
          
          ]

# create window object
window = pysg.Window("SQL Movie Library Catalog", layout, use_default_focus=False, 
                     resizable=True, finalize=True)



# set event loop
while True: 

    # read window for events and collect values
    event, values = window.read()

    # if user clicks exit or the exit button in top right of window, end loop
    if event in (None, "Exit"):
        break
    
    if event in "create":
        hide_elements(window)
        print("Perform create function.")

    elif event in "read":
        show_read_elements(window)
        print("Perform read function")

    elif event in "update":
        hide_elements(window)
        print("Perform update function")

    elif event in "delete":
        hide_elements(window)
        show_delete_elements(window)
        print("Perform delete function")
    
    
    
    # if user enters data in the input field, copy that into the output field
    # if event in ("Execute"):
    #     window["list"].update(values["name_in"])

# close window and end program
window.close()
