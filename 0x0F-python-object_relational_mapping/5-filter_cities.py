#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Result: takes in the name of a state
as an argument and lists all cities
of that state, using the database
hbtn_0e_4_usa
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
    c.execute("""SELECT cities.name
                 FROM cities
                 JOIN states
                 ON cities.state_id = states.id
                 WHERE states.name = %s
                 ORDER BY cities.id;""", (query,))
    res = c.fetchall()
    for n in range(len(res)):
        if n != 0:
            print(", ", end='')
        if n is not None:
            print(res[n][0], end='')
    print('')
    c.close()
    db.close()
