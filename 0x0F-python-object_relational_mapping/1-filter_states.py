#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Result: lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    host = "localhost"

    db = MySQLdb.connect(host=host,
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'""")
    res = c.fetchall()
    for n in res:
        print(n)
    c.close()
    db.close()
