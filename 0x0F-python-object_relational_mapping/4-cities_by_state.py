#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    nme = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=usr,
                         passwd=pwd, db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id \
                 ORDER BY c.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
