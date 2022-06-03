#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    charHide = dir(hidden_4)
    line = len(charHide)
    for n in range(0, line):
        valeur = charHide[n]
        if valeur[:2] != "__":
            print("{}".format(valeur), end="\n")
