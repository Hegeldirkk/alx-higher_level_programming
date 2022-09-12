#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Result: lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys as sqlarg
    
    db = MySQLdb.connect(host="localhost",port=3306,user=sqlarg.argv[1],passwd=sqlarg.argv[2],db=sqlarg.argv[3])

    c=db.cursor()
    c.execute("""SELECT *  FROM states ORDER BY id""")
    res = c.fetchall()
    for n in res:
        print(n)

