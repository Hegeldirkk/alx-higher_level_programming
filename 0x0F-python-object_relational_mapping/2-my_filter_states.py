#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Result: takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where
name matches the argument.
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    host = "localhost"
    query = argv[4]

    db = MySQLdb.connect(host=host,
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name='{:s}'""".format(query))
    res = c.fetchall()
    for n in res:
        print(n)
    c.close()
    db.close()
