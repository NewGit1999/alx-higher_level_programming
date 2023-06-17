#!/usr/bin/python3
"""that takes in an argument and displays all values in the states table"""
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    nme = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=usr,
                         passwd=pwd, db=database, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states
                   WHERE name LIKE BINARY '{}'
                   ORDER BY id".format(nme))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
