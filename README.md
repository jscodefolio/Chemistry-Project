# Chemistry-Project
This project uses SQLite3 with Python and Pandas to access a database of Elements.
The user is able to request the Atomic Weight of an element by entering any identifying information (Atomic Number, Name or Symbol). The program will process the user input to determine which field to search. This was a simple project to get a feel for SQL.

INSTRUCTIONS?:

Wrote SQL commands to .sql file to create a database for the Table of Elements.
in Terminal:
Move to root directory with SQLite shell (.exe)
From .sql file, create database

$ sqlite3

$ sqlite elementsDB.db < createElementsDB.sql


NOTES:
The get_info() function currently does not take user input and should be rewritten to accept and reformat (syntactically) user input for use in the query string with a similar if/else block to determine which fields to query.










