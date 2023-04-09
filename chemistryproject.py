# TO DO:
# 1-- Make user input NOT case sensitive
# 2-- Process user input against all fields of Table
        #so results can be found with any info without needing separate prompts
# 3-- Write functions whose parameters are user input.
        # so I can call the functions from the shell to get info without prompts

import sqlite3
from sqlite3 import Error
import pandas as pd

db = ("C:\\sqlite\\elementsDB.db")


def create_connection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return conn



#Uses Pandas to format dataframe for display
def see_all(conn):
    query = "SELECT * FROM elements"
    df = pd.read_sql_query(query,conn)
    pd.set_option('display.max_rows', None) #over rides pandas default to display 5 rows in dataframe to instead show all
    print(df)


# TODO: Make filter1 a generic array or list, if possible have output print to separate window from shell input/feedback info
def get_info(conn):
    filter1 = "('Hydrogen','Boron')"
    query = ("SELECT * FROM elements WHERE Name IN " + filter1 + " ")
    df = pd.read_sql_query(query,conn)
    print(df.head())

def run_query(query):
    return pd.read_sql_query(query,db)

# lots of repetitive code
def get_mass(conn):
    user_input = input("Atomic Mass request for: ")
      
    try:
        string_int = int(user_input)
        if isinstance(string_int, int):
            number = (str(user_input),)
            cur = conn.cursor()
            cur.execute("SELECT AtomicMass FROM elements WHERE AtomicNumber = ?", number)
            result = cur.fetchone()[0]
            print(result)

    except ValueError:
            
        if len(user_input) > 3:
            name = (str(user_input),)
            cur = conn.cursor()
            cur.execute("SELECT AtomicMass FROM elements WHERE Name = ?", name)
            result = cur.fetchone()[0]
            print(result)

        elif len(user_input)<=3:
            symbol = (str(user_input),)
            cur = conn.cursor()
            cur.execute("SELECT AtomicMass FROM elements WHERE Symbol = ?", symbol)
            result = cur.fetchone()[0]
            print(result)

def main():
    conn = create_connection(db)
    
    with conn:
        
        get_mass(conn)
        get_info(conn)
        


if __name__=='__main__':
    main()
















# OLD FUNCTIONS (for reference because this was a learning project) replaced with getMass()

def from_name_get_mass(conn):
    user_input = input("Atomic Mass request for: ")
    name = (str(user_input),)
    query = ("SELECT AtomicMass FROM elements WHERE Name = ?")
    cur = conn.cursor()
    cur.execute(query, name)
    result = cur.fetchone()[0]
    print(result)



def from_num_get_mass(conn):
    user_input = input("Atomic Mass request for: ")    
    number = (str(user_input),)
    query = "SELECT AtomicMass FROM elements WHERE AtomicNumber = ?"
    cur = conn.cursor()
    cur.execute(query, number)
    result = cur.fetchone()[0]

    print(result)
