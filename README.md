# Chemistry-Project
The user is able to request the Atomic Weight of an element by entering any identifying information (Atomic Number, Name or Symbol). The program will process the user input to determine which field to search. This was a simple project to get a feel for SQL.

### INSTRUCTIONS:

**Creating the database**

In the root directory which should contain SQLite.exe run the following:

`>> sqlite3`

or whatever version you're using.

`>> sqlite nameOfYourDataBase.db < createElementsDB.sql`



**NOTES:**

The get_info() function currently does not take user input and should be rewritten to accept and reformat (syntactically) user input for use in the query string with a similar if/else block to determine which fields to query.










