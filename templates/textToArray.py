from numpy import loadtxt

def textToArray(filename):
    with open(filename, "rb") as file:
        data = loadtxt(filename, comments="#", delimiter=" ", unpack=False)
    return data