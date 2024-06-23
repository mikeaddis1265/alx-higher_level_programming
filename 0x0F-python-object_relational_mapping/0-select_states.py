#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", usr=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cu = db.cursor()  # Corrected variable name
    cu.execute("SELECT * FROM states ORDER BY id ASC")  # Corrected variable name
    rows = cu.fetchall()  # Corrected variable name
    for row in rows:
        print(row)
    cu.close()  # Corrected variable name
    db.close()
