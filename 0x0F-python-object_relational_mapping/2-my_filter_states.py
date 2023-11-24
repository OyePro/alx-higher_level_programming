#!/usr/bin/python3

"""
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
parameters given to script include: username, password, database, name in order
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """connect to database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """create cursor to execute queries using sql"""
    nm = argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (nm,))

    """getting result from cursor"""
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
