# Chemistry-Project
This project uses SQLite3 in conjunction with Python and Pandas to access elemental data from a database of the Periodic Table of Elements.
The user is able to request the Atomic Weight of an element by entering any identifying information (Atomic Number, Name or Symbol). The program will process the user input to determine which field to search.
The value is returned as an integer and readily available to be used in mathematical calculations.
This program can be extended by adding other elemental fields to the database and writing similar functions to access those records, however, this project was originally started for personal use in a Chemistry class that finished before this program and has now instead become a practice on working with SQLite and Python. 
Additional functions and database changes are unlikely to be added at this time.

Some functions need to be rewritten and cleaned up.
There are unused functions left behind for personal reference.
The if/else statement in the try/except clause is clunky and cluttered.
The get_info() function currently does not take user input but should be rewritten to accept and reformat (syntactically) user input for use in the query string with a similar if/else block to determine which fields to query.








Wrote SQL commands to .sql file to create a database for the Table of Elements.
in Terminal:
Move to root directory with SQLite shell (.exe)
From .sql file, create database

>> sqlite3
>> sqlite elementsDB.db < createElementsDB.sql



