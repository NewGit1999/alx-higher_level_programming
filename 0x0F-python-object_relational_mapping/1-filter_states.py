#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)"""
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=usr,
                         passwd=pwd, db=database, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name
                   LIKE BINARY '%N' ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
