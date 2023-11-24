#!/usr/bin/python3

"""
a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
parameters given to script include: username, password, database in order
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """connect to database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """create cursor to execute queries using sql"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    """getting result from cursor"""
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
