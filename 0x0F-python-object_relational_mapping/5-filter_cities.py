#!/usr/bin/python3

"""
a script that list all cities of a state using database hbtn_0e_4_usa
it takes in the name of the state as an argument
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
    cur.execute("""SELECT cities.name
                 FROM cities
                 INNER JOIN states
                 ON cities.state_id = states.id
                 WHERE states.name = %s
                 ORDER BY cities.id ASC""", (nm,))

    """getting result from cursor"""
    lists = ()
    for row in cur.fetchall():
        lists += row
    for i in range(len(lists)):
        if i < (len(lists) - 1):
            print(lists[i], end=", ")
        else:
            print(lists[i])
    cur.close()
    db.close()
