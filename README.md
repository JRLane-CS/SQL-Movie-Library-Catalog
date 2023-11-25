# Overview

SQL Movie Library Catalog is an application which stores the names and locations of all movies in one's collection of BluRays, DVDs, or videotapes. The location is stored by bookcase, shelf, and, in the case of there being stacks of movies atop the bookcase, the stack number. This way, even if the stacks on top of a bookcase are turned in such a way that the movie case spine is not visible, you'll still know approximately where to find your movie.

## Description
The SQL Movie Library Catalog allows for the addition of new titles, searching of all titles, updating a title, and deleting a title. It accepts input from the user for each of these operations and performs the task according to what the user selects and inputs.

## Purpose
I have a growing collection of DVD and BluRay discs. I tried to keep track of them using a spreadsheet, but it is so time consuming to update the data, organize it, and then print out new catalogs. Over time, it got to the point that the task was so onerous that I simply stopped doing it. 

This is where the idea for the SQL Movie Library Catalog comes in: The moment a movie or show is added into the database, it is available for search. No longer would I have to print out the catalogs! Instead, all that is necessary is to type enough of the title into the search input and the database is accessed to locate where the movie or show is located (along with any others that match the search term in some way). Not only this, but I no longer have to worry about whether the title starts with a 'The', 'A', 'An', or any other word. The program will almost instantaneously locate the title as I type.

## Video Demo
{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The relational database used in this application is the SQLite3 module which is built into Python.

The movies.db is set up with two tables. The movies table is arranged with five columns:
- the id (Primary key)
- the movie title (FOREIGN KEY)
- the bookcase where the disc is stored
- the shelf where the disc is stored
- the stack if the disc is on top of the bookcase

The extended table is arranged with three columns:
- the movie title (PRIMARY KEY)
- the year the movie came out
- the imdb id of the title

In the Search Joined Tables feature, the type of join is an INNER JOIN between the two tables.

# Development Environment

Microsoft's Visual Studio Code was the IDE on which this program was coded.

Python is the programming language used to develop this application. It is configured with the PySimpleGUI and SQLite modules.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [PySimpleGUI Tutorial](https://www.youtube.com/watch?v=LzCfNanQ_9c)
- [PySimpleGUI Tutorials](https://www.youtube.com/playlist?list=PL1A5nGiCuucueLRBA0VKHIjYTYipHqzcZ)
- [PySimpleGUI Documentation](https://www.pysimplegui.org/en/latest/)
- [Python SQLite Tutorial](https://www.youtube.com/watch?v=pd-0G0MigUA)
- [SQLite Databases with Python: Full Course](https://www.youtube.com/watch?v=byHcYRpMgI4)
- [SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)

# Future Work

Although the SQL Movie Library Catalog is functional, it is also limited in what it does. I intend to expand these capabilities in the future. Some of the improvements I intend to make include:

- access an API to collect all the statistics of a given movie and store that in this application
- adapt to use a code reader, to automate the API access and storage of information
- create a separate table to hold the media type of a given movie
- create a separate table to hold the actor/actress names 
- create a separate table to hold the movie ratings
- create a separate table to hold the movie categories
- modify search operation to search on title, actor/actress, movie rating, and movie categories
