# import gui library
import PySimpleGUI as pysg

# import sql library
import sqlite3

# import csv library
import csv

# read movie csv file into list
# create an empty list.
movie_list = []

# prepare for error and read csv file into movie_list
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

# handle any errors, print out the error message, end program
except Exception as e:
    print(f"Error reading movies.csv\n{e}\n")
    exit()

# create the connection to and set up the database if it doesn't exist
connection = sqlite3.connect("movies.db")

# create the cursor 
cur = connection.cursor()

# if movies.db tables do not exist, create them
cur.execute("""
            CREATE TABLE IF NOT EXISTS movies 
            (id int PRIMARY KEY, title text, bookcase int, shelf int, stack int)
            """)

# loop through movies list and format according to db layout
for i, movie_row in enumerate(movie_list):
    
    # if stack is None, set as zero, otherwise change text to int
    if movie_row[3] != "":
        movie_list[i][3] = int(movie_row[3])
    else:
        movie_list[i][3] = 0

# if movies are not in the db, insert them
cur.executemany("INSERT OR IGNORE INTO movies VALUES (?, ?, ?, ?, ?)", movie_list)
connection.commit()

# set gui color scheme
pysg.theme("darkbrown7")


# function to create the window to add a movie (db create operation)
def create_window():
    
    # set the layout for the create window
    create_layout = [
        [pysg.Text("Add movie title:"), 
        pysg.Input(key="title", expand_x=True)],
        [pysg.Text("Location:")],
        [pysg.Text("Bookcase number:"), 
        pysg.Input(key="bookcase", expand_x=True)],
        [pysg.Text("Shelf number:"), 
        pysg.Input(key="shelf", expand_x=True)],
        [pysg.Text("Stack number:"), 
        pysg.Input(key="stack", expand_x=True)],
        [pysg.Text("Output:"), 
        pysg.Multiline
        (key="list", size=(0, 5), expand_x=True, expand_y=True, pad=11)],
        [pysg.Button("Add Movie", key="add_movie"), 
         pysg.Button("Exit Add Movie", key="exit")],
    ]
    
    # start create window object
    create_window = pysg.Window("SQL Movie Library Catalog", create_layout, 
                use_default_focus=False, resizable=True, finalize=True, 
                modal=True)

    # event loop for create window
    while True:

        # read create window for events and collect values
        event, values = create_window.read()

        # if user clicks exit button or the red x in top right of window, end
        if event in (None, "exit"):
            break
        
        # read (list) movies in db based on search term
        elif event in "add_movie":
            
            # clear any former comments from output
            create_window["list"].Update("")

            # load variables with input data
            title = values["title"]
            bookcase = values["bookcase"]
            shelf = values["shelf"]
            stack = values["stack"]
            validity = True

            # error check the movie title for being empty
            if title == "":
                create_window["list"].print("Title is required!")
                validity = False                

            # verify bookcase is an integer
            if not bookcase.isdecimal():
                create_window["list"].print("Bookcase must be an integer!")
                validity = False

            else:
                bookcase = int(bookcase)

            # either shelf or stack must be populated, not both
            if (shelf == "" and stack == "") or \
               (shelf.isdecimal() == False and stack.isdecimal() == False):
                create_window["list"].print("Valid shelf or stack is required!")
                validity = False

            # set shelf or stack integers
            if shelf.isdecimal() and stack.isdecimal():
                shelf = int(shelf)
                stack = int(stack)
                
                # default to shelf value if both > 0
                if shelf > 0 and stack > 0:
                    stack = 0

            # if shelf is a decimal, then make stack 0
            elif shelf.isdecimal():
                shelf = int(shelf)
                stack = 0

            # otherwise make stack the integer and shelf 0
            elif stack.isdecimal():
                stack = int(stack)
                shelf = 0

            # check to make sure that stack and shelf are not both zero
            if stack == 0 and shelf == 0:
                create_window["list"].print("Invalid location.")
                validity = False

            # if there were errors, loop again
            if not validity:
                continue
                
            # default to shelf value if both > 0
            if shelf > 0 and stack > 0:
                stack = 0
                
            # get next available primary key to insert into db
            key = 1
            for value in cur.execute("SELECT * FROM movies"):
                if value[0] == (key):
                    key += 1
                else:
                    break

            # load movie list with db elements
            movie_list = [key, title, bookcase, shelf, stack,]

            # insert movie into db
            cur.execute("INSERT OR IGNORE INTO movies VALUES \
                        (?, ?, ?, ?, ?)", movie_list)
            connection.commit() 

            # break out of loop and close window
            break

    # close the read window and end function
    create_window.close()
    

# function to create the window to search the db (db read operation)
def read_window():
    
    # set the layout for the read window
    read_layout = [
        [pysg.Text("Search:"), 
        pysg.Input(key="title", enable_events=True, expand_x=True)],
        [pysg.Text("Output:", key="output_text", size=(5, 20)), 
        pysg.Multiline(key="list", expand_x=True, expand_y=True, pad=11)],
        ]
    
    # start the read window object
    read_window = pysg.Window("SQL Movie Library Catalog", read_layout, 
                  use_default_focus=False, resizable=True, finalize=True, 
                  modal=True)
    
    # event loop to read the read window
    while True:

        # read the read window for events and collect values
        event, values = read_window.read()

        # if user clicks exit button or the red x in top right of window, end
        if event in (None, "Exit"):
            break
        
        # read (list) movies in db based on search term
        elif event in "title":
            
            # get search value(s)
            search = values["title"]

            # clear the multiline element output
            read_window["list"].Update("")

            # loop through the db, display any partial matches to search value
            for movie_data in cur.execute("SELECT * FROM movies"):
                if search in movie_data[1]:
                    if movie_data[4] == 0:
                        read_window["list"].print(f"'{movie_data[1]}', {movie_data[2]}, {movie_data[3]}")
    
                    else:
                        read_window["list"].print(f"'{movie_data[1]}', {movie_data[2]}, {movie_data[3]}, {movie_data[4]}")
    # close the read window and end function
    read_window.close()


# TODO function to create the window to update a db entry (db update operation)
def update_window():
    
    update_layout = [

    ]
    
    # update movie by id
    cur.execute("SELECT * FROM movies WHERE id = ?", (key,))
    print(f"\n Before update:\n{cur.fetchall()}")
    cur.execute("UPDATE movies SET title = ? WHERE id = ?", (title, key,))
    connection.commit()
    cur.execute("SELECT * FROM movies WHERE id = ?", (key,))
    print(f"\n After update:\n{cur.fetchall()}")


# TODO function to create the window to delete a db entry (db delete operation)
def delete_window():

    delete_layout = [

    ]

    # have user select the movie to delete, get key from db, delete by key
    key = 0
    
    # delete movie by id
    cur.execute("DELETE FROM movies WHERE id = ?", (key,))
    connection.commit()
    cur.execute("SELECT * FROM movies WHERE id = ?", (key,))
    print(f"\n After deleting id {key}:\n{cur.fetchall()}\n")

# set initial gui layout
initial_layout = [
    [pysg.Push(), pysg.Text("Select Database Operation (CRUD):"), pysg.Push()], 
    [pysg.Button("Add Movie", key="create",enable_events=True), 
     pysg.Button("Search Movies", key="read", enable_events=True), 
     pysg.Button("Update Movie", key="update", enable_events=True), 
     pysg.Button("Delete Movie", key="delete", enable_events=True)],
    [pysg.Push(), pysg.Button("Quit", key="quit"), pysg.Push()],
    ]

# create initial window object to select CRUD operation on db
window = pysg.Window("SQL Movie Library Catalog", initial_layout, 
                     use_default_focus=False, resizable=True, finalize=True)

# set main event loop
while True: 

    # read window for events and collect values
    event, values = window.read()

    # if user clicks exit or the exit button in top right of window, end loop
    if event in (None, "quit"):
        break
    
    if event in "create":
        create_window()

    elif event in "read":
        read_window()

    elif event in "update":
        print("Perform update function")

    elif event in "delete":
        print("Perform delete function")

# close window and end program
window.close()
