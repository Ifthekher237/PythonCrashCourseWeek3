#this program prints out the first alphabet of evey word of a given string.
def acronym(string):
    for x in string.split():
        print(x[0].upper(),end="")


acronym("universal serial bus")
