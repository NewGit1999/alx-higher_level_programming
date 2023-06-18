#!/usr/bin/python3
"""sql injection"""
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
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY %(name)s \
                 ORDER BY states.id ASC", {'name': nme})
    rows = cur.fetchall()
    for row in rows:
        print(row)
