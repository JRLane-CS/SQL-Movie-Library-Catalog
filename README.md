# Overview

SQL Movie Library Catalog is an application which stores the names and locations of all movies in one's collection of BluRays, DVDs, or videotapes. The location is stored by bookcase, shelf, and, in the case of there being stacks of movies atop the bookcase, the stack number. This way, even if the stacks on top of a bookcase are turned in such a way that the movie case spine is not visible, you'll still know where to find your movie.

{Provide a description of the software that you wrote and how it integrates with a SQL Relational Database. Describe how to use your program.}

{Describe your purpose for writing this software.}

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The relational database used in this application is the SQLite module in Python.

{Describe the structure (tables) of the relational database that you created.}

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
- create a separate table to hold the actors/actresses 
- create a separate table to hold the movie ratings
- create a separate table to hold the movie categories
